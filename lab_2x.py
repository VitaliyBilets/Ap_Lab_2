import unittest


def has_three_sum(arr, P):
    n = len(arr)

    # Перебираємо всі можливі трійки
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == P:
                    return True

    return False


class TestThreeSum(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(has_three_sum([1, 2, 3], 6))
        self.assertFalse(has_three_sum([1, 2, 4], 6))
        self.assertTrue(has_three_sum([10, 20, 30, 40, 50], 90))
        self.assertFalse(has_three_sum([5, 1, 3, 7, 9], 100))
        self.assertTrue(has_three_sum([3, 3, 3, 3], 9))
        self.assertFalse(has_three_sum([1, 1, 1], 10))


if __name__ == "__main__":
    unittest.main()
