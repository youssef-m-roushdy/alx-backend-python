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
        self.assertEqual(access_nested_map(nested_map, path), expected)
