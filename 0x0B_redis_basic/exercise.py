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
    def inner(self, *args, **kwargs) -> str:
        """ Inner function for count """
        self._redis.incr(method.__qualname__)
        val = method(self, *args, **kwargs)
        return val
    return inner


def call_history(method: Callable) -> Callable:
    """ History of function calls """
    @wraps(method)
    def inner(self, *args, **kwargs) -> str:
        """ Inner function for history """
        name = method.__qualname__
        inp = name + ":inputs"
        outp = name + ":outputs"
        self._redis.rpush(inp, str(args))
        val = method(self, *args, **kwargs)
        self._redis.rpush(outp, val)
        return val
    return inner


def replay(method: Callable) -> None:
    """ Get information for a function call """
    self = method.__self__
    name = method.__qualname__
    inp = name + ":inputs"
    outp = name + ":outputs"
    count = self._redis.get(name).decode()
    inp = self._redis.lrange(inp, 0, -1)
    outp = self._redis.lrange(outp, 0, -1)
    print(name + ' was called ' + count + ' times:')
    zipped = zip(inp, outp)
    zipped = list(zipped)
    for pair in zipped:
        res = '(*' + pair[0].decode() + ')'
        print(name + res + ' -> ' + pair[1].decode())


class Cache():
    """ Cache system with Redis """
    def __init__(self):
        """ Initialize the class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
        """ Get a string from Redis """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Get and integer from Redis """
        return self.get(key, int)
