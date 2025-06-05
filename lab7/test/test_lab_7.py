import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import lab_7


class TestRabinKarp(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(lab_7.rabin_karp("abcabcabc", "abc"), [0, 3, 6])

    def test_no_match(self):
        self.assertEqual(lab_7.rabin_karp("abcdefgh", "xyz"), [])

    def test_overlap(self):
        self.assertEqual(lab_7.rabin_karp("aaaaaa", "aaa"), [0, 1, 2, 3])

    def test_single_char(self):
        self.assertEqual(lab_7.rabin_karp("abcde", "c"), [2])

    def test_pattern_longer_than_text(self):
        self.assertEqual(lab_7.rabin_karp("abc", "abcd"), [])


if __name__ == '__main__':
    unittest.main()
