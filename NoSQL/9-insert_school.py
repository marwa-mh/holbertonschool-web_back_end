#!/usr/bin/env python3
""" 8-all """
import pymongo


def insert_school(mongo_collection: pymongo, **kwargs):
    """Insert new document"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
