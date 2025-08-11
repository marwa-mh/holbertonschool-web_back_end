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
        """return the appropriate page of the dataset"""
        if not isinstance(page, int) or not isinstance(page_size, int):
            raise AssertionError("The value should be integer")
        assert page > 0
        assert page_size > 0
        data = self.dataset()
        (start, end) = index_range(page, page_size)
        return data[start:end]
    """
    page_size: the length of the returned dataset page
    page: the current page number
    data: the dataset page (equivalent to return from previous task)
    next_page: number of the next page, None if no next page
    prev_page: number of the previous page, None if no previous page
    total_pages: the total number of pages in the dataset as an integer
    """
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """get hyper method"""
        if isinstance(page, float) and page.is_integer():
            page = int(page)
        if isinstance(page_size, float) and page_size.is_integer():
            page_size = int(page_size)
        if not isinstance(page, int) or not isinstance(page_size, int):
            raise AssertionError("The value should be integer")
        data = self.get_page(page, page_size)
        result = dict()
        result["page_size"] = len(data)
        result["page"] = page
        result["data"] = data
        if page * page_size < len(self.dataset()):
            result["next_page"] = page + 1
        else:
            result["next_page"] = None
        if page > 1:
            result["prev_page"] = page - 1
        else:
            result["prev_page"] = None
        result["total_pages"] = math.ceil(len(self.dataset()) / page_size)
        return result
