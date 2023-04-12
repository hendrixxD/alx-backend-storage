#!/usr/bin/env python3
"""
Task 10. Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    args:
        mongo_collection
        name
        topics
    return count
    """
    # Update the documents with the name
    update_result = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    # Return the number of documents updated
    return update_result.modified_count

