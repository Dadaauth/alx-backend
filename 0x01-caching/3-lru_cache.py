#!/usr/bin/env python3
"""This is my module documentation"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """This is my class documentation"""

    def __init__(self):
        super().__init__()
        self.usecount = {}

    def put(self, key, item):
        """This is my function docuemntation """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.usecount[key] = 0
        if len(self.cache_data) > self.MAX_ITEMS:
            leastRecentlyUsed = list(self.usecount)[0]
            for key in self.usecount.keys():
                if self.usecount[key] < self.usecount[leastRecentlyUsed]:
                    leastRecentlyUsed = key
            print(f"DISCARD: {leastRecentlyUsed}")
            self.cache_data.pop(leastRecentlyUsed)
            self.usecount.pop(leastRecentlyUsed)
            for key in self.usecount.keys():
                self.usecount[key] = 0


    def get(self, key):
        """This is my function documentation"""
        if key is None or key not in self.cache_data:
            return None
        self.usecount[key] += 1
        return self.cache_data[key]
