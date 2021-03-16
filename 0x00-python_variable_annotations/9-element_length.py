#!/usr/bin/env python3
""" Annotating a function """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Adding types to function """
    i: int = 1
    return [(i, len(i)) for i in lst]
