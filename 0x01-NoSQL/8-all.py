#!/usr/bin/env python3
"""
a Python function that lists all documents in a collection
"""
def list_all(mongo_collection):
    """
    a Python function that lists all documents in a collection
    """
    # Find all documents in the collection
    all_documents = mongo_collection.find()
    
    # Convert cursor to list
    all_documents_list = list(all_documents)
    
    return all_documents_list if all_documents_list else []
