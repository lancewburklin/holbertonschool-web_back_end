#!/usr/bin/env python3
"""
Returning wait times from wait_random
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Like wait_n but with a task """
    res: List[float] = []
    t = max_delay
    for c in asyncio.as_completed([task_wait_random(t) for i in range(0, n)]):
        item = await c
        res.append(item)
    return res
