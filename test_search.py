#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from search import linear_search, binary_search


class TestLinearSearch(unittest.TestCase):
    def setUp(self):
        self.data = [1, 10, 20, 34, 56, 75, 78, 89, 100]

    def test_search(self):
        for i, v in enumerate(self.data):
            with self.subTest(i=i):
                self.assertEqual(linear_search(self.data, v), i)

    def test_larger(self):
        self.assertEqual(linear_search(self.data, -10), None)

    def test_smaller(self):
        self.assertEqual(linear_search(self.data, 1000), None)

    def test_not_found(self):
        self.assertEqual(linear_search(self.data, 35), None)


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.data = [1, 10, 20, 34, 56, 75, 78, 89, 100]

    def test_search(self):
        for i, v in enumerate(self.data):
            with self.subTest(i=i):
                self.assertEqual(binary_search(self.data, v), i)

    def test_larger(self):
        self.assertEqual(binary_search(self.data, -10), None)

    def test_smaller(self):
        self.assertEqual(binary_search(self.data, 1000), None)

    def test_not_found(self):
        self.assertEqual(binary_search(self.data, 35), None)

if __name__ == '__main__':
    unittest.main()
