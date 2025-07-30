#!/usr/bin/env python3
"""Module """
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Generator that sleeps 10 times then returns random float"""

    result = [value async for value in async_comprehension()]
    return result
