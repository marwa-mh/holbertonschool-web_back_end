#!/usr/bin/env python3
""" 8-main """


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection: a PyMongo collection object.

    Returns:
        List of documents (each is a dict). Empty list if no documents.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
