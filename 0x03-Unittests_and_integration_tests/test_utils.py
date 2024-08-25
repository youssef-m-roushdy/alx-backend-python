#!/usr/bin/env python3
"""
Unit tests for the access_nested_map function.
"""
from unittest import TestCase
from parameterized import parameterized
access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(TestCase):
    @parameterized.expand([
        ("test1", {"a": 1}, ("a",), 1),
        ("test2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("test3", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        """
        Test the access_nested_map function with different inputs.

        Args:
            name (str): The name of the test case.
            nested_map (dict): The nested dictionary to access.
            path (tuple): The keys path to access in the nested map.
            expected (Any): The expected result from the function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
