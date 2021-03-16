#!/usr/bin/env python3
""" Measuring the runtime of a function """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Just Measuring the time it takes to run wait_n """
    t0 = time.time()
    asyncio.run(wait_n(n, max_delay))
    t1 = time.time()
    res: float = (t1 - t0) / n
    return res
