import unittest

import solve


class TestSolveFunction(unittest.TestCase):
    def test_valid_input(self):
        # Test a word without repeating letters
        self.assertTrue(solve("education"))

    def test_invalid_input(self):
        # Test a word with repeating letters
        self.assertFalse(solve("hello"))

    def test_empty_input(self):
        # Test an empty string
        self.assertTrue(solve(""))

    def test_non_alpha_input(self):
        # Test a word with non-alphabet characters
        self.assertTrue(solve("word123"))

if __name__ == '__main__':
    unittest.main()