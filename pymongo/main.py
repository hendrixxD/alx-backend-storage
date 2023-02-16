#!/usr/bin/env python3
"""intro to pymongo in python 
"""

from pymongo import MongoClient

client = MongoClient()
# print(client)

# specifying setting assides the default
client = MongoClient(host='localhost', port=27017)

# MongoDB URI format
client = MongoClient('mongodb://localhost:27017')

db = client.names
# print(db)

# another way to access names db 
# using dict-style
db = client['names']

tutorial1 = {
     "title": "Working With JSON Data in Python",
     "author": "Lucas",
     "contributors": [
         "Aldren",
         "Dan",
         "Joanna"
     ],
     "url": "https://realpython.com/python-json/"
}

# an instance of names
name = db.name
# print(name)

result = name.insert_one(tutorial1)
print(result)
