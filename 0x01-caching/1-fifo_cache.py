#!/usr/bin/python3
"""Module that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """class that inherits from BaseCaching and is a caching system"""
    def put(self, key, item):
        """Adds items to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                rem = list(self.cache_data.keys())[0]
                del self.cache_data[rem]
                print("DISCARD: {}".format(rem))

    def get(self, key):
        """Returns the item using the key"""
        return self.cache_data.get(key, None)
