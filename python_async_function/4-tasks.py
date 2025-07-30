#!/usr/bin/env python3
"""Module """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """calls wait_random n number of times"""
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))  # Tasks already running

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
