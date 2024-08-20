#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns indexed data to make the pagination deletion resilient"""
        keys_data = []
        dataset = self.indexed_dataset()
        index = 0 if index is None else index
        assert index >= 0 and index <= len(dataset)
        [keys_data.append(i) for i in dataset.keys()
         if i >= index and len(keys_data) <= page_size]
        next_index = keys_data[-1] if len(keys_data) - page_size == 1 else None
        return {
            'index': index,
            'data': [dataset[i] for i in keys_data[:-1]],
            'page_size': page_size,
            'next_index': next_index
        }
