#!/usr/bin/python3
"""Module that builds LRU Cache Replacement"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Class that implements LRU cache replacement"""
    def __init__(self):
        """Initialize properties for the class"""
        super().__init__()
        self.__keys = []
        self.__Rlock = RLock()

    def put(self, key, item):
        """Adds items to the cache"""
        if key is not None and item is not None:
            keyOut = self.remove_ele(key)
            with self.__Rlock:
                self.cache_data[key] = item
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        """Returns an item by key"""
        with self.__Rlock:
            value = self.cache_data.get(key, None)
            if key in self.__keys:
                self.remove_ele(key)
        return value

    def remove_ele(self, keyIn):
        """Removes the items from the dictionary when the limit hits"""
        keyrem = None
        with self.__Rlock:
            keysLength = len(self.__keys)
            if keyIn not in self.__keys:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyrem = self.__keys.pop(0)
                    self.cache_data.pop(keyrem)
            else:
                self.__keys.remove(keyIn)
            self.__keys.insert(keysLength, keyIn)
        return keyrem
