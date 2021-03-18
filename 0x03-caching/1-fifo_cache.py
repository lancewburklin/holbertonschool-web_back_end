#!/usr/bin/env python3
"""
FIFO caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First in, first out, with a limit
    """
    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                items = list(self.cache_data.keys())
                print("DISCARD: " + items[0])
                del self.cache_data[items[0]]
                self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None:
            return None
        return self.cache_data.get(key)
