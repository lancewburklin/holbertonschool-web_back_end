#!/usr/bin/env python3
""" Creating a list with a type """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Getting the sum of a float list """
    sum: float = 0
    for i in input_list:
        sum = sum + i

    return sum
