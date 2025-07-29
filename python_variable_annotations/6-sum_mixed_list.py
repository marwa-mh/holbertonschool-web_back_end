#!/usr/bin/env python3
"""
This module contain a function sum_list
"""
from typing import Union, List


def sum_mixed_list(mxd_lst:List[Union[int, float]]) -> float:
    """return sum of list"""
    return sum(mxd_lst)
