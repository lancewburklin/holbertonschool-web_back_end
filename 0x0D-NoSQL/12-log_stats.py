#!/usr/bin/env python3
""" Get nginx stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collect = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    deleteR = collect.count_documents({"method": "DELETE"})
    print("{} logs".format(collect.count_documents({})))
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(
                                      method,
                                      collect.count_documents(
                                            {'method': method})))
    print("{} status check".format(
        collect.count_documents({'method': "GET", 'path': '/status'})))
