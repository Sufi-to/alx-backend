#!/usr/bin/python3
"""Module that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class that inherits from basic caching"""
    def put(self, key, item):
        """Adds items to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the item using the key"""
        return self.cache_data.get(key, None)
