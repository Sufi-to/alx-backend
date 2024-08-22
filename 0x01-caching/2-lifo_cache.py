#!/usr/bin/python3
"""Module that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """class that inherits from BaseCaching and is a caching system"""
    elements_in = []

    def put(self, key, item):
        """Adds items to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.__class__.elements_in.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                rem = self.__class__.elements_in[-2]
                del self.cache_data[rem]
                print("DISCARD: {}".format(rem))

    def get(self, key):
        """Returns the item using the key"""
        return self.cache_data.get(key, None)
