#!/usr/bin/env python3
"""Basic Redis class
"""
import redis
from uuid import uuid4
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable):
        """ Decode Redis item """
        item = self._redis.get(key)
        if fn is None:
            return item
        return fn(item)
