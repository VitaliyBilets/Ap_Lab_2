import unittest
import tempfile
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import lab_8




class TestLab8(unittest.TestCase):
    def setUp(self):

        self.test_csv = tempfile.NamedTemporaryFile(delete=False, mode='w', newline='')
        self.test_csv.write("0,1,0\n1,0,2\n0,2,0\n")
        self.test_csv.close()
        self.expected_matrix = [
            [0.0, 1.0, 0.0],
            [1.0, 0.0, 2.0],
            [0.0, 2.0, 0.0]
        ]

    def tearDown(self):
        os.unlink(self.test_csv.name)

    def test_read_adjacency_matrix(self):
        matrix = lab_8.read_adjacency_matrix(self.test_csv.name)
        self.assertEqual(matrix, self.expected_matrix)

    def test_build_graph(self):
        matrix = self.expected_matrix
        G = lab_8.build_graph(matrix)
        self.assertEqual(set(G.nodes), {0, 1, 2})
        self.assertEqual(set(G.edges), {(0, 1), (1, 2)})
        self.assertEqual(G[0][1]['weight'], 1.0)
        self.assertEqual(G[1][2]['weight'], 2.0)

if __name__ == '__main__':
    unittest.main()
