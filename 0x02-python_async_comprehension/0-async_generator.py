#!/usr/bin/env python3
""" Creating random numbers """
import asyncio
from random import uniform


async def async_generator() -> None:
    """ Creating an async generator """
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
