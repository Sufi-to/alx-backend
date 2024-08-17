#!/usr/bin/env python3
"""Module for returning data from the csv file in a paginated way."""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page, page_size):
        """
        Returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
        """
        return ((page - 1) * page_size, page*page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the list of data from the required page"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        info = self.dataset()
        index_ran = self.index_range(page, page_size)
        if index_ran[1] > len(info)-1:
            return []
        return info[index_ran[0]: index_ran[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a dictionary containing the following key-value pairs"""
        total_data = len(self.dataset())
        data = self.get_page(page, page_size)
        total_page = math.ceil(total_data / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_page else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_page": total_page
        }
