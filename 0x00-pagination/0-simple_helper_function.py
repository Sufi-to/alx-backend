#!/usr/bin/env python3
"""Module that implements a simple pagination"""


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
