import unittest
from NAKAJIMA_AYAKA_2 import edit_distance, suggestions


class TestEditDistance(unittest.TestCase):

    def test_simple_substitution(self):
        dist, table = edit_distance("cat", "cut")
        self.assertEqual(dist, 1)

    def test_empty_to_word(self):
        dist, table = edit_distance("", "abc")
        self.assertEqual(dist, 3)

    def test_word_to_empty(self):
        dist, table = edit_distance("abcd", "")
        self.assertEqual(dist, 4)

    def test_table_values(self):
        dist, table = edit_distance("abc", "adc")
        self.assertEqual(dist, 1)
        self.assertEqual(table[1][1], 0)  # "a" vs "a"
        self.assertEqual(table[2][2], 1)  # "ab" vs "ad"
        self.assertEqual(table[3][3], 1)  # "abc" vs "adc"

    # suggestions test
    def test_suggestions_exact(self):
        result = suggestions("cat")
        self.assertIn("cat", result)

if __name__ == "__main__":
    unittest.main()
