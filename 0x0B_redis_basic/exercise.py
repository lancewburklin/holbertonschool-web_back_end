#!/usr/bin/env python3
"""Basic Redis class
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count calls decorator """
    @wraps(method)
    def inner(*args, **kwargs):
        args[0]._redis.incr(method.__qualname__)
        val = method(*args, **kwargs)
        return val
    return inner


class Cache():
    """ Cache system with Redis """
    def __init__(self):
        """ Initialize the class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data with a random key """
        ranKey = str(uuid4())
        self._redis.mset({ranKey: data})
        return ranKey

    def get(self, key: str, fn: Optional[Callable] = None):
        """ Decode Redis item """
        item = self._redis.get(key)
        if fn is None:
            return item
        return fn(item)

    def get_str(self, key: str) -> str:
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        return self.get(key, int)
