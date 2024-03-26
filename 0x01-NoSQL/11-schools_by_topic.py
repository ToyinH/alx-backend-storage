#!/usr/bin/env python3
"""
Python function that returns the list of school having a specific topic
"""
def schools_by_topic(mongo_collection, topic):
    """
    Python function that returns the list of school having a specific topic
    """
    # Find all documents in the collection with the given topic
    schools = mongo_collection.find({"topics": topic})
    
    # Convert cursor to list
    schools_list = list(schools)
    
    return schools_list
