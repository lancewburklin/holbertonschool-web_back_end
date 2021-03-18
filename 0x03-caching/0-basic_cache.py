#!/usr/bin/env python3
"""
Basic FIFO caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic chaching with no limit """
    def put(self, key, item):
        """
        Create the cache item
        """
        if (key is None or item is None):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get a cached item based on key
        """
        if (key is None):
            return None
        return self.cache_data.get(key)
