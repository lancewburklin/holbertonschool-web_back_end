#!/usr/bin/env python3
"""
LRU caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Last recently used, with a limit
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
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                if len(self.order) == 0:
                    self.order[key] = 1
                else:
                    num = max(list(self.order.values())) + 1
                    self.order[key] = num
            else:
                items = list(self.cache_data.keys())
                if key in items:
                    self.cache_data[key] = item
                    for lock, val in self.order.items():
                        if val > self.order[key]:
                            self.order[lock] -= 1
                    self.order[key] = self.MAX_ITEMS
                else:
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
        if self.cache_data.get(key) is None:
            return None
        for item, val in self.order.items():
            if val > self.order[key]:
                self.order[item] = val - 1
        self.order[key] = 4
        return self.cache_data.get(key)
