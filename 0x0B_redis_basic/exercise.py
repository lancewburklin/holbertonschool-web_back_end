#!/usr/bin/env python3
"""Basic Redis class
"""
import redis
from uuid import uuid4
from typing import Union


class Cache():
    """ Cache system with Redis """
    def __init__(self):
        """ Initialize the class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data with a random key """
        ranKey = str(uuid4())
        self._redis.mset({ranKey: data})
        return ranKey
