#!/usr/bin/python3
"""Module that implements LFU cache replacement system"""

from collections import defaultdict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Class that implements LFU cache system"""
    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.freq = defaultdict(int)
        self.order_key = {}
        self.time_freq = 0

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lfu_key = min(self.freq,
                              key=lambda k: (self.freq[k], self.order_key[k]))
                print(f"DISCARD: {lfu_key}")
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
                del self.order_key[lfu_key]

            self.cache_data[key] = item
            self.freq[key] = 1
        self.time_freq += 1
        self.order_key[key] = self.time_freq

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.time_freq += 1
        self.order_key[key] = self.time_freq
        return self.cache_data[key]
