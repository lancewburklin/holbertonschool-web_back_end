#!/usr/bin/env python3
""" Testing the utils module """
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json
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


class TestGetJson(unittest.TestCase):
    """ Test the get_json method """
    @parameterized.expand([
        ["http://example.com", {"payload": True}],
        ["http://holberton.io", {"payload": False}],
    ])
    def test_get_json(self, url, payload):
        """ Test get_json method """
        with patch('requests.get') as the_patch:
            the_patch.return_value = Mock()
            the_patch.return_value.json.return_value = payload
            res = get_json(url)
            self.assertEqual(res, payload)


if __name__ == '__main__':
    unittest.main()
