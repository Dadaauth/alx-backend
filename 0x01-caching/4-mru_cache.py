#!/usr/bin/env python3
"""This is my module documentation"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """This is my class documentation"""

    def __init__(self):
        """My __init__ function"""
        super().__init__()
        self.usecount = {}

    def put(self, key, item):
        """This is my function docuemntation """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.usecount) == 0:
            self.usecount[key] = 0
        else:
            self.usecount[key] = max(self.usecount.values()) + 1
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            delkey = sorted(self.usecount, key=self.usecount.get)[-2]
            print(f"DISCARD: {delkey}")
            self.usecount.pop(delkey)
            self.cache_data.pop(delkey)

    def get(self, key):
        """This is my function documentation"""
        if key is None or key not in self.cache_data:
            return None
        self.usecount[key] = max(self.usecount.values()) + 1
        return self.cache_data[key]
