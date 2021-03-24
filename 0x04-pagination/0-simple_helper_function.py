#!/usr/bin/env python3
"""
Pagination helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
	""" Returning page info """
    info: Tuple = ((page * page_size) - page_size, (page_size * page))
    return info
