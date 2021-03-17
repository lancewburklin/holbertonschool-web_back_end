#!/usr/bin/env python3
""" Creating random numbers """
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Creating an async generator """
    for i in range(10):
        await asyncio.sleep(1)
        num: float = uniform(0, 10)
        yield num
