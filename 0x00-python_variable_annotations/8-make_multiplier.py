#!/usr/bin/env python3
"""
Module 8-make_multiplier
"""
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Reterive a function"""
    def func(a: float) -> float:
        """Reterive a product of multiplier and number"""
        return a * multiplier
    return func
