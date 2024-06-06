from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database
class Book(BaseModel):
    id: int
    title: str
    author: str

books_db = [
    Book(id=1, title="1984", author="George Orwell"),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee"),
]

# Get all books
@app.get("/books", response_model=List[Book])
def get_books():
    return books_db

# Get a specific book by ID
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Add a new book
@app.post("/books", response_model=Book, status_code=201)
def add_book(book: Book):
    print(book)
    books_db.append(book)
    return book

# Update a book by ID
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            books_db[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# Delete a book by ID
@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            del books_db[i]
            return
    raise HTTPException(status_code=404, detail="Book not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)