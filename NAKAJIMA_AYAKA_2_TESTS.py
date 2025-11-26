import unittest
from NAKAJIMA_AYAKA_2 import edit_distance


class TestEditDistance(unittest.TestCase):

    def test_simple_substitution(self):
        dist, table = edit_distance("cat", "cut")
        print("test_simple_substitution")
        print("Dist cat->cut:", dist)
        print("Table cat->cut:", table)
        self.assertEqual(dist, 1)
    
    def test_from_class_example(self):
        dist, table = edit_distance("sun", "sns")
        print("test_from_class_example")
        print("Dist sun->sns:", dist)
        print("Table sun->sns:", table)
        self.assertEqual(dist, 2)
    
    def test_from_class_example_reverse(self):
        dist, table = edit_distance("sns", "sun")
        print("test_from_class_example_reverse")
        print("Dist sns->sun:", dist)
        print("Table sns->sun:", table)
        self.assertEqual(dist, 2)

    def test_empty_to_word(self):
        print("test_empty_to_word")
        dist, table = edit_distance("", "abc")
        print("Dist empty->abc:", dist)
        print("Table empty->abc:", table)
        self.assertEqual(dist, 3)

    def test_word_to_empty(self):
        print("test_word_to_empty")
        dist, table = edit_distance("abcd", "")
        print("Dist abcd->empty:", dist)
        print("Table abcd->empty:", table)
        self.assertEqual(dist, 4)

    def test_table_values(self):
        print("test_table_values")
        dist, table = edit_distance("abc", "adc")
        print("Dist abc->adc:", dist)
        print("Table abc->adc:", table)
        self.assertEqual(dist, 1)
        self.assertEqual(table[1][1], 0)  # "a" vs "a"
        self.assertEqual(table[2][2], 1)  # "ab" vs "ad"
        self.assertEqual(table[3][3], 1)  # "abc" vs "adc"
    


if __name__ == "__main__":
    unittest.main()
