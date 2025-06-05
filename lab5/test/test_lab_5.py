import unittest
import os
import sys

# Додаємо шлях до src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import lab_5


class TestLab5(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_input.txt"
        with open(self.test_file, "w") as f:
            f.write("0,0\n")
            f.write("2,2\n")
            f.write("3,3\n")
            f.write("[1 1 0]\n")
            f.write("[0 1 0]\n")
            f.write("[1 1 1]\n")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_input_file(self):
        start, end, matrix = lab_5.read_input_file(self.test_file)
        self.assertEqual(start, (0, 0))
        self.assertEqual(end, (2, 2))
        expected_matrix = [
            [1, 1, 0],
            [0, 1, 0],
            [1, 1, 1]
        ]
        self.assertEqual(matrix, expected_matrix)

    def test_dfs_finds_path(self):
        _, _, matrix = lab_5.read_input_file(self.test_file)
        path = lab_5.dfs(matrix, (0, 0), (2, 2))
        self.assertTrue(path)
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (2, 2))

    def test_dfs_no_path(self):
        matrix = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]
        path = lab_5.dfs(matrix, (0, 0), (2, 2))
        self.assertEqual(path, [])


if __name__ == '__main__':
    unittest.main()
