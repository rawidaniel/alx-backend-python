#!/usr/bin/env python3
"""
Module 101-safely_get_value
"""
from typing import Sequence, Union, Any, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Reterive value fro a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
