#!/usr/bin/env python3
"""Module """
import typing
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Generator that sleeps 10 times then returns random float"""
    start = time.perf_counter()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    
    return end - start
