#!/usr/bin/env python3
"""A documentation for my module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A class documentation"""

    def put(self, key, item):
        """A function documentation"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            last = list(self.cache_data)[-2]
            print(f"DISCARD: {last}")
            self.cache_data.pop(last)

    def get(self, key):
        """A function documentation"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
