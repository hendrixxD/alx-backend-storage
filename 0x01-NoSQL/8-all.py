#!/usr/bin/env python3
"""
Task 8. List all documents in Python
"""


def list_all(mongo_collection):
    """
    args:
        mongo_collection -> mongo collection object
    """
    documents = mongo_collection.find()
    documents =list(documents)

    return documents if documents else []
