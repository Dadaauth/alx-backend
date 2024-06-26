#!/usr/bin/env python3
"""A module documentation that I wrote"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class documentation that I wrote"""

    def put(self, key, item):
        """A function documentation that I wrote"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """A function documentation that I wrote"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
