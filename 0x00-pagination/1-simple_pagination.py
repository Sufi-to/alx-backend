import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    if page == 0:
        return (1, page_size)

    if page > 0:
        return ((page-1)*page_size, page*page_size)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the list of data from the required page"""
        try:
            assert page > 0 and page_size > 0
        except Exception:
            raise AssertionError
        info = self.dataset()
        index_ran = index_range(page, page_size)
        if index_ran[1] > len(info)-1:
            return []
        return [info[i] for i in range(index_ran[0], index_ran[1])]
