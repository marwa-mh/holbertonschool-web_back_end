#!/usr/bin/env python3
"""Method to return the index range"""


def index_range(page: int, page_size: int):
    """return the range of indexes """

    return ((page - 1) * page_size, page * page_size)
