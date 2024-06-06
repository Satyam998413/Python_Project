from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os

# MongoDB settings
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = "bookstore"

app = FastAPI()

# MongoDB client
client = AsyncIOMotorClient(MONGODB_URL)
db = client[DATABASE_NAME]

# Pydantic models
class Book(BaseModel):
    id: str = Field(default_factory=str, alias="_id")
    title: str
    author: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Helper function to convert a MongoDB document to a Pydantic model
def book_helper(book) -> Book:
    return Book(**book)

# Route to get all books
@app.get("/books", response_model=List[Book])
async def get_books():
    books = []
    async for book in db.books.find():
        books.append(book_helper(book))
    return books

# Route to get a specific book by ID
@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: str):
    book = await db.books.find_one({"_id": ObjectId(book_id)})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_helper(book)

# Route to add a new book
@app.post("/books", response_model=Book, status_code=201)
async def add_book(book: Book):
    new_book = await db.books.insert_one(book.dict(by_alias=True))
    created_book = await db.books.find_one({"_id": new_book.inserted_id})
    return book_helper(created_book)

# Route to update a book by ID
@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: str, updated_book: Book):
    updated_data = {k: v for k, v in updated_book.dict(by_alias=True).items() if v is not None}
    result = await db.books.update_one({"_id": ObjectId(book_id)}, {"$set": updated_data})
    if result.modified_count == 1:
        updated_book = await db.books.find_one({"_id": ObjectId(book_id)})
        return book_helper(updated_book)
    raise HTTPException(status_code=404, detail="Book not found")

# Route to delete a book by ID
@app.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: str):
    result = await db.books.delete_one({"_id": ObjectId(book_id)})
    if result.deleted_count == 1:
        return
    raise HTTPException(status_code=404, detail="Book not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)