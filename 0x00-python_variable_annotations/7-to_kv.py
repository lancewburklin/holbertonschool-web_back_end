#!/usr/bin/env python3
""" Returning a more complex tuple """
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Taking in two different possible types """
    new_tuple: Tuple[str, float] = (k, v**2)
    return new_tuple
