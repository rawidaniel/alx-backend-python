#!/usr/bin/env python3
"""
Module test_utils
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """
    A class that defint test for accessNestedMap function
    """
    @parameterized.expand([({"a": 1}, ['a'], 1),
                           ({"a": {"b": 2}}, ['a'], {"b": 2}),
                           ({"a": {"b": 2}}, ['a', 'b'], 2)])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: Any) -> None:
        """Test accessNestedMap function
        Parameters
        ----------
        nested_map: Mapping
            A nested map
        path: Sequence
            a sequence of key representing a path to the value
        """
        self.assertEqual(access_nested_map(nested_map, path), result)


if __name__ == "__main__":
    unittest.main()
