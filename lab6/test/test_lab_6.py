import unittest
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import lab_6


class TestLab6(unittest.TestCase):
    def setUp(self):
        # Створюємо тестовий файл
        self.test_file = "test_dependencies.txt"
        with open(self.test_file, "w") as f:
            f.write("A B\n")
            f.write("A C\n")
            f.write("B D\n")
            f.write("C D\n")

    def tearDown(self):
        # Видаляємо тестовий файл після тестів
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_dependencies(self):
        graph, in_degree = lab_6.read_dependencies(self.test_file)
        expected_graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D"]
        }
        self.assertEqual(dict(graph), expected_graph)
        self.assertEqual(in_degree["D"], 2)
        self.assertEqual(in_degree["A"], 0)

    def test_topological_sort(self):
        graph, in_degree = lab_6.read_dependencies(self.test_file)
        order = lab_6.topological_sort(graph, in_degree.copy())
        self.assertEqual(set(order), {"A", "B", "C", "D"})
        self
