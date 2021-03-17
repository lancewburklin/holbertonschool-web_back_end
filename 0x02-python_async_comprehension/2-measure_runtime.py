#!/usr/bin/env python3
""" Measuring the runtime of async_comp """
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run the generator asyncrinously and measure the runtime """
    t0 = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    t1 = time.time()
    res: float = t1 - t0
    return (t1 - t0)
