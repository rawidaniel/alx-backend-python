#!/usr/bin/env python3
"""
Module test_utils
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import (
    Mapping,
    Sequence,
    Any,
)
from unittest.mock import patch
import json


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

    @parameterized.expand([({}, ['a']), ({"a": 1}, ['a', 'b'])])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """Test accessNestedMap function for exception raise
        Parameters
        ----------
        nested_map: Mapping
            A nested map
        path: Sequence
            a sequence of key representing a path to the value
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    A class that represent test for get_json function
    """
    @parameterized.expand([("http://example.com", {"payload": True}),
                          ("http://holberton.io", {"payload": False})])
    def test_get_json(self, test_url, test_payload):
        """Test a get_json function to ensure it returns the expexted result

        Parameters
        ----------
        test_url: str
            url to send http request to
        test_payload: json
            expected json response
        """
        with patch('utils.requests.get') as mock_request_get:
            mock_request_get.return_value.json.return_value = test_payload
            response = get_json(test_url)
            mock_request_get.assert_called_with(test_url)
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """
    A class that represent test for memoize function
    """
    def test_memoize(self):
        """Test utils.memoize decorated work as intended
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once()


if __name__ == "__main__":
    unittest.main()
