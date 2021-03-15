#!/usr/bin/env python3
""" Returning a callable type """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return a callable that multiplies """
    def mult(m: float) -> float:
        """ Multiplies the m to multiplier """
        return m * multiplier
    return mult
