#!/usr/bin/env python3
"""My module documentation"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """A function documentation is always necessary!"""
    start_idx = 0
    end_idx = 0
    for _ in range(1, page):
        start_idx += page_size
    end_idx += start_idx + page_size
    return (start_idx, end_idx)


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
        """Page getting function"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert int(page) > 0
        assert int(page_size) > 0
        idx_rage = index_range(page, page_size)
        data = self.dataset()
        return data[idx_rage[0]:idx_rage[1]]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        data = self.get_page(page, page_size)
        dataset = self.dataset()
        rtn_dict = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < (len(dataset) / page_size) else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": math.ceil(len(dataset) / page_size)
        }
        return rtn_dict
