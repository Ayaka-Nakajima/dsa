'''
combine (Tree(f1, e1, r1), Tree(f2, e2, r2)) = Tree(f1 + f2, x, y)
tree= Leaf of (int, char)
        | Node of (int, tree, tree)
for each (char, int) in table:
    put Leaf(int, char)  into priority queue

while queue has at least two entries:
    pop two smallest entries
    combine them into a Tree and add tree to the queue
    return single entry of the queue
'''