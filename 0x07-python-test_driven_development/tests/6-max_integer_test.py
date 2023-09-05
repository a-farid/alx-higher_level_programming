#!/usr/bin/python3
"""This module to find the max integer in a list
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Suite test for max_integer function
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([8, -5, 10, 6]), 10)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_repeated_number(self):
        self.assertEqual(max_integer([100, 100, 100]), 100)

    def test_float_numbers(self):
        self.assertEqual(max_integer([500, 510, 500, 490]), 510)

    def test_max_operated_integer(self):
        self.assertEqual(max_integer([-35, -55 * -55, 125, -15]), 255)

    def test_neg_numbers(self):
        self.assertEqual(max_integer([-100, -50, -20, -10]), -10)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([50, 40, 30, 20, 10]), 50)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_list_with_loop(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_big_list(self):
        self.assertEqual(max_integer([
            501, 502, 503, 504, 505, 506, 507, 508, 509, 510,
            511, 512, 513, 514, 515, 516, 517, 518, 519, 520,
            1000, 518, 517, 516, 515, 514, 513, 512, 511, 510,
            509, 508, 507, 506, 505, 504, 503, 502, 501]), 1000)
