#!/usr/bin/env python3
"""Method to return the index range, class Server"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """Method index range"""
    return ((page - 1) * page_size, page * page_size)


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
        if not isinstance(page, int) or not isinstance(page_size, int):
            raise AssertionError("The value should be integer")
        assert page > 0
        assert page_size > 0
        data = self.dataset()
        (start, end) = index_range(page, page_size)
        return data[start:end]
