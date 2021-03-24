#!/usr/bin/env python3
"""
Simple pagination list
"""
import csv
import math
from typing import List, Tuple
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initialize function """
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
        """ Get the requested pages """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        data: List = []
        items: Tuple = (index_range(page, page_size))
        allData = self.dataset()
        i: int = items[0]
        while i != items[1] and i < len(allData):
            data.append(allData[i])
            i += 1
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Getting pages with additional info """
        data = self.get_page(page, page_size)
        hyper: dict = {}
        hyper['page_size'] = len(data)
        hyper['page'] = page
        hyper['data'] = data
        if (page + 1) * page_size <= len(self.dataset()):
            hyper['next_page'] = page + 1
        else:
            hyper['next_page'] = None
        if (page == 1):
            hyper['prev-page'] = None
        else:
            hyper['prev-page'] = page - 1
        hyper['total_pages'] = math.ceil(len(self.dataset()) / page_size)
        return hyper
