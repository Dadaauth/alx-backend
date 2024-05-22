#!/usr/bin/env python3
"""A module documentation that I wrote"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A documentation for my class"""

    def put(self, key, item):
        """Inserts new data into the cache"""
        if item is None or key is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first = list(self.cache_data.keys())[0]
            print(f"DISCARD: {first}")
            self.cache_data.pop(first)

    def get(self, key):
        """Gets a data from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
