#!/usr/bin/env python3
"""
This module contain a function sum_list
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
