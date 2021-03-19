#!/usr/bin/env python3
"""
FIFO caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First in, first out, with a limit
    """
    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.order = {}

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            pass
        else:
            things = list(self.cache_data.keys())
            if key in things:
                for lock, val in self.order.items():
                    if val > self.order[key]:
                        self.order[lock] = val - 1
                num = max(list(self.order.values())) + 1
                self.order[key] = num
                self.cache_data[key] = item
                return
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                if len(self.order) == 0:
                    self.order[key] = 1
                else:
                    num = max(list(self.order.values())) + 1
                    self.order[key] = num
            else:
                items = list(self.cache_data.keys())
                temp = None
                for lock, val in self.order.items():
                    if val == 1:
                        print('DISCARD: ' + lock)
                        del self.cache_data[lock]
                        temp = lock
                    else:
                        self.order[lock] = val - 1
                if temp:
                    del self.order[temp]
                self.order[key] = self.MAX_ITEMS
                self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None:
            return None
        return self.cache_data.get(key)
