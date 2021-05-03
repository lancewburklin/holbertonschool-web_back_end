#!/usr/bin/env python3
""" List collections in MOngoDB """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ List all in a collection """
    items = []
    mongo_collection = mongo_collection.find()
    for x in mongo_collection:
        items.append(x)
    return items
