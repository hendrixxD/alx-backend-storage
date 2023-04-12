#!/usr/bin/env python3
"""
Task advanced task
"""


from pymongo import MongoClient

client = MongoClient()

# Assign the database name to a variable
db_name = "mydb"

# Connect to the database
db = client[db_name]

# Select the collection
collection = db.school

# Find all documents with name starting with "Holberton"
documents = collection.find({"name": {"$regex": "^Holberton"}})

# Convert the cursor to a list
documents = list(documents)

# Print the list of documents
print(documents)
