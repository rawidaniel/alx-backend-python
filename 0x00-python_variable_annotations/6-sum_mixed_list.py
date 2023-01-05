#!/usr/bin/env python3
"""
Module 6-sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Reterive the summation of the element in the list"""
    sum: float = 0
    for item in mxd_lst:
        sum += item
    return sum
