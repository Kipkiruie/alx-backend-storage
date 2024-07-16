#!/usr/bin/env python3
"""Module to insert a new document into a MongoDB collection."""

import pymongo

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    
    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object.
    **kwargs: Arbitrary keyword arguments representing the fields and values of the document.
    
    Returns:
    ObjectId: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
