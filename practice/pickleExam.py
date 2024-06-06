import pickle
 
# initializing data to be stored in db
Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 
'age' : 21, 'pay' : 40000}
Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
'age' : 50, 'pay' : 50000}
 
# database
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish
 
# For storing
# type(b) gives <class 'bytes'>;
b = pickle.dumps(db)   
print("Byte code",b)
# For loading
myEntry = pickle.loads(b)
print("Object code",myEntry)