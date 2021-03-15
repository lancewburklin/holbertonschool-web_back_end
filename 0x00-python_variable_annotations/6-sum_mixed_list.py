#!/usr/bin/env python3
""" Get the sum of a mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Get the sum of mxd_list """
    the_sum: float = 0
    for i in mxd_lst:
        the_sum = the_sum + i
    return the_sum
