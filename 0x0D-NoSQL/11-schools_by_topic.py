#!/usr/bin/env python3
""" Get a list of schools with topic """
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ Get collections with topic """
    schools = mongo_collection.find()
    allSchhols = []
    for school in schools:
        topics = school.get('topics')
        if topics:
            if topic in topics:
                allSchhols.append(school)
    return allSchhols
