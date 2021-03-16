#!/usr/bin/env python3
""" Using a random wait before executing """
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    num = uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
