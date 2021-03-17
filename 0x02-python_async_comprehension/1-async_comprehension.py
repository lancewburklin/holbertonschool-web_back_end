#!/usr/bin/env python3
""" Collecting numbers from an async generator """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collecting generator results """
    result: List = [i async for i in async_generator()]
    return result
