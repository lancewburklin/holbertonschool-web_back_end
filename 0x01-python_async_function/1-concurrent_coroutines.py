#!/usr/bin/env python3
"""
Returning wait times from wait_random
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """ One result at a time, concurrently """
    res = []
    t = max_delay
    for c in asyncio.as_completed([wait_random(t) for i in range(0, n)]):
        item = await c
        res.append(item)
    return res
