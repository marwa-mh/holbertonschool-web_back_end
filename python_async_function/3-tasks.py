#!/usr/bin/env python3
"""Module """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """calls wait_random """

    return asyncio.Task(wait_random(max_delay))
