#!/usr/bin/env python3
"""Module """
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """calls wait_random n number of times"""
    delays = asyncio.run(wait_n(n, max_delay))
    result = sum(delays) / n
    return result
