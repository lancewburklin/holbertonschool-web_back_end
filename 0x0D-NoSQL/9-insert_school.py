#!/usr/bin/env python3
""" Insert a new Document """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ Insert a document """
    newOne = mongo_collection.insert(kwargs)
    return newOne
