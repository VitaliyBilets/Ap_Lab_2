import unittest
from lab2.lab_2 import three_sum
class TestThreeSum(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(three_sum([1, 2, 3], 6))
        self.assertFalse(three_sum([1, 2, 4], 6))
        self.assertTrue(three_sum([1, 4, 45, 6, 10, 8], 22))
        self.assertFalse(three_sum([1, 2, 3, 4, 5], 50))
        self.assertTrue(three_sum([-1, 0, 1, 2, -1, -4], 0))

if __name__ == "__main__":
    unittest.main()