import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        data: List = []
        items = index_range(page, page_size)
        allData = self.dataset()
        if (items[0] > len(allData)):
            return data
        if (items[1] > len(allData)):
            items[1] = len(allData)
        i = items[0]
        while i < items[1]:
            onePage = []
            while len(onePage) != page_size:
                onePage.append(allData[i])
                i += 1
            data.append(onePage)
        return data[0]
