import unittest
import math
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from lab_9 import max_wire_length

class TestMaxWireLength(unittest.TestCase):
    def test_equal_heights(self):
        self.assertEqual(max_wire_length(1, [1, 1]), round(math.hypot(1, 0), 2))
