#!/usr/bin/env python3
"""
This module contain a function element_length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """func element length"""
    return [(i, len(i)) for i in lst]
