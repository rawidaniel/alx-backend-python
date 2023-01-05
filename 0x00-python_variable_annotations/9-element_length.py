#!/usr/bin/env python3
"""
Module 9-element_length
"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """reterive a list of tuple contatining the sequence and it's lenght"""
    return [(i, len(i)) for i in lst]
