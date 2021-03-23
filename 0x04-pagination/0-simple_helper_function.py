#!/usr/bin/env python3
"""
Pagination helper function
"""


def index_range(page, page_size):
    return ((page * page_size) - page_size, (page_size * page))
