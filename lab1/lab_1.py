import unittest

def way(matrix):

    if matrix == [] or matrix[0] == []:
        return []

    result = []


    for i in range(len(matrix)):
        row = matrix[i]


        if i % 2 == 0:
            result.extend(row)
        else:

            result.extend(row[::-1])

    return result

class TestGardenerRoute(unittest.TestCase):
    def test_case_1(self):
        m = 5
        n = 5
        grid = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [
            1, 2, 3, 4, 5, 10, 9, 8, 7, 6,
            11, 12, 13, 14, 15, 20, 19, 18, 17, 16,
            21, 22, 23, 24, 25
        ]
        self.assertEqual(way(grid), expected)

    def test_case_2(self):
        m = 2
        n = 4
        grid = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        expected = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(way(grid), expected)

    def test_case_3(self):
        m = 1
        n = 4
        grid = [
            [1, 2, 3, 4]
        ]
        expected = [1, 2, 3, 4]
        self.assertEqual(way(grid), expected)

    def test_case_4(self):
        m = 6
        n = 1
        grid = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(way(grid), expected)

if __name__ == "main":
    unittest.main()