#!/usr/bin/env python3
"""4. MRU Caching
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching
    """

    def __init__(self):
        """the init method
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign the dictionary self.cache_data
        the item value for the key key
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            _key = list(self.cache_data)[-1]
            print(f'DISCARD: {_key}')
            del self.cache_data[_key]

        self.cache_data[key] = item 
        

    def get(self, key):
        """retrieves values given a key
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
