#!/usr/bin/env python3
"""
Task 9. Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    ars:
        mongo_collection

    return -> id
    """
    # Insert the document into the collection
    insert_result = mongo_collection.insert_one(kwargs)
    # Return the _id of the new document
    return insert_result.inserted_id
