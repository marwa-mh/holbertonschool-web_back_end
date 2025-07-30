#!/usr/bin/env python3
"""Module """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generator that sleeps 10 times then returns random float"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
