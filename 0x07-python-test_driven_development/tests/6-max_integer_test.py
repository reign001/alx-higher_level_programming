#!/usr/bin/python3
import unittest

def max_integer(lst=[]):
    """Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None
    """
    if len(lst) == 0:
        return None
    result = lst[0]
    i = 1
    while i < len(lst):
        if lst[i] > result:
            result = lst[i]
        i += 1
    return result

class TestMaxIntegerFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]), "Empty list should return None")

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 5, 3, 8, 2]), 8, "Incorrect result for positive numbers")

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -8, -2]), -1, "Incorrect result for negative numbers")

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 5, -3, 8, -2]), 8, "Incorrect result for mixed numbers")

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.9, 3.2]), 3.2, "Incorrect result for float numbers")

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3, "Incorrect result for duplicate numbers")

if __name__ == '__main__':
    unittest.main()

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
