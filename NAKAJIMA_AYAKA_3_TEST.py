
from NAKAJIMA_AYAKA_3 import tree_of_codes, huffman_decode
from huffmandecode import codes, string

# test1
codes1 = {
    "a": "0",
    "b": "1",
}
tree1 = tree_of_codes(codes1)

assert tree1 == ("a", "b")

assert huffman_decode("0", tree1) == "a"
assert huffman_decode("1", tree1) == "b"
assert huffman_decode("101", tree1) == "bab"


# test2

codes2 = {
    "a": "0",
    "b": "10",
    "c": "11",
}
tree2 = tree_of_codes(codes2)
assert tree2 == ("a", ("b", "c"))

# 0 1 0 1 1 → a b a c
assert huffman_decode("01011", tree2) == "abc"


# test3
codes3 = {
    "A": "00",
    "B": "01",
    "C": "10",
    "D": "11",
}
tree3 = tree_of_codes(codes3)
assert tree3 == (("A", "B"), ("C", "D"))

# 00 01 10 11 → A B C D
assert huffman_decode("00011011", tree3) == "ABCD"

# test4 with professor's example codes
tree4 = tree_of_codes(codes)
assert huffman_decode("0010010100", tree4) == "hg"
