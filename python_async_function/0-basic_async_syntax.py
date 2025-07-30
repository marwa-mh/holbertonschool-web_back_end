#!/usr/bin/env python3
"""Module """
import asyncio
from random import random


async def wait_random(max_delay: int = 10):
    """Wait for random amount of time"""
    delay = random() * max_delay
    asyncio.sleep(delay)
    return delay
