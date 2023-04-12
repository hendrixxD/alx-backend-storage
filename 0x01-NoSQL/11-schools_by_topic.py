#!/usr/bin/env python3
"""
Task 11. Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
    args:
        mongo_collection
        topic
    return -> list
    """
    # Find all documents with the specified topic
    documents = mongo_collection.find({"topics": topic})
    # Convert the cursor to a list
    documents = list(documents)
    # Return the list of documents
    return documents if documents else []
