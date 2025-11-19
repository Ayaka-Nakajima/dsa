
from NAKAJIMA_AYAKA_3 import tree_of_codes, huffman_decode
from huffmandecode import codes, string

# ---- Test 1: 最も単純な 2 文字 ----
codes1 = {
    "a": "0",
    "b": "1",
}
tree1 = tree_of_codes(codes1)
# 木の形は ('a', 'b') のはず
assert tree1 == ("a", "b")

assert huffman_decode("0", tree1) == "a"
assert huffman_decode("1", tree1) == "b"
assert huffman_decode("101", tree1) == "bab"


# ---- Test 2: 3 文字で、片側がさらに分岐する木 ----
# 例: a:0, b:10, c:11 → 木: ('a', ('b', 'c'))
codes2 = {
    "a": "0",
    "b": "10",
    "c": "11",
}
tree2 = tree_of_codes(codes2)
assert tree2 == ("a", ("b", "c"))

# 0 1 0 1 1 → a b a c
assert huffman_decode("01011", tree2) == "abac"


# ---- Test 3: 4 文字で完全二分木 ----
# A:00, B:01, C:10, D:11
# 木: (('A', 'B'), ('C', 'D'))
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

tree4 = tree_of_codes(codes)
decoded4 = huffman_decode(string, tree4)

expected = (
    "Statt des toerichten Ignorabimus heisse im Gegenteil unsere Losung: "
    "Wir muessen wissen, wir werden wissen."
)