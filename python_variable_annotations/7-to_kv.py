#!/usr/bin/env python3
"""
This module contain a function sum_list
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return sum of list"""
    result = (k, v**2)
    return result
