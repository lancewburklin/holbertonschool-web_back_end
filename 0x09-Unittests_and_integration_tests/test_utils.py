#!/usr/bin/env python3
""" Testing the utils module """
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ Test Access Nested Map """
    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {'b': 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2],
    ])
    def test_access_nested_map(self, map, path, res):
        """ Test the access nested map """
        self.assertEqual(access_nested_map(map, path), res)

    @parameterized.expand([
        [{}, ("a",), "'a'"],
        [{"a": 1}, ("a", "b"), "'b'"]
    ])
    def test_access_nested_map_exception(self, map, path, res):
        """ Test an Exception """
        with self.assertRaises(KeyError) as kE:
            access_nested_map(map, path)
        self.assertEqual(str(kE.exception), res)


if __name__ == '__main__':
    unittest.main()
