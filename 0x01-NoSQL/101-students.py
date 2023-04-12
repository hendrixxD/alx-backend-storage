#!/usr/bin/env python3
"""
Task 14. Top students
"""


def top_students(mongo_collection):
    """
    args:
        mongo_collection

    return -> list
    """
    # Find all students and sort by average score
    students = mongo_collection.aggregate([
        {"$project": {"name": 1, "averageScore": {"$avg": "$scores.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
    # Convert the cursor to a list
    students = list(students)
    # Return the list of students
    return students if students else []
