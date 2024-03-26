#!/usr/bin/env python3
"""
Python function that changes all topics of a school document based on the name
"""
def update_topics(mongo_collection, name, topics):
    """
    Python function that changes all topics of a school document based on the name
    """

    # Update all documents with the given school name to have the new list of topics
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

