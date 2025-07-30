#!/usr/bin/env python3
"""Module """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
async def wait_n(n: int, max_delay: int ) -> List[float]:
    """calls wait_random n number of times"""
    delays = []
    tasks = []
    for x in range(n):
        tasks.append(wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
