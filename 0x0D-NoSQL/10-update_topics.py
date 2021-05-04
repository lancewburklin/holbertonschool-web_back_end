#!/usr/bin/env python3
""" Updating Topics """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """ Upfate mongo collection """
    values = {'name': name}
    newValues = {"$set": {"topics": topics}}
    mongo_collection.update_one(values, newValues)
