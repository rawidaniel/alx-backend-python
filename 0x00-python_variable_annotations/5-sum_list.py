#!/usr/bin/env python3
"""
Module 5-sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Reterive the summation of the element in the list"""
    sum: float = 0
    for item in input_list:
        sum += item
    return sum
