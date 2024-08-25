#!/usr/bin/env python3
"""
Unit tests for functions.
"""
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize


class TestAccessNestedMap(TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map function with different inputs.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The keys path to access in the nested map.
            expected (Any): The expected result from the function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, error):
        """
        Test that access_nested_map raises the expected exception.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The keys path to access in the nested map.
            error (Exception): The expected exception type to be raised.

        Raises:
            AssertionError: If the expected exception is not raised.
        """
        with self.assertRaises(error):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function to ensure it returns the correct JSON payload.

        Args:
            mock_get (Mock): The mock object for requests.get.
            test_url (str): The URL to be used in the test.
            test_payload (dict): The JSON payload should be returned by mock.

        Asserts:
            The result of get_json should match the test_payload.
        """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(TestCase):
    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                """
                Method return 42
                """
                return 42

            @memoize
            def a_property(self):
                """
                Property return 42 from a_method
                """
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()


if __name__ == '__main__':
    unittest.main()
