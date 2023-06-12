#!/usr/bin/env python
from emails import find_email
import unittest


class TestFile(unittest.TestCase):
    def test_basic(self):
        test_case = [None, 'David', 'Miller']
        expected = 'davidmiller@example.com'
        self.assertEqual(find_email(test_case), expected)

    def test_one_name(self):
        test_case = [None, 'Jennifer']
        expected = 'Missing parameters'
        self.assertEqual(find_email(test_case), expected)

    def test_two_name(self):
        test_case = [None, 'Lisa', 'Clark']
        expected = 'No email address found'
        self.assertEqual(find_email(test_case), expected)


if __name__ == '__main__':
    unittest.main()
