#!/usr/bin/env python3
""" Measuring the runtime of async_comp """
import time
import asyncio
a = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run the generator asyncrinously and measure the runtime """
    t0 = time.time()
    await asyncio.gather(a(), a(), a(), a())
    t1 = time.time()
    return (t1 - t0)
