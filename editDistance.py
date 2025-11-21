"""
Edit distance
Two strings x= x1...xm, y=y1...yn
1. deleting a character
2. inserting a character
3. changing a character

x = sunny
y = snowy

E(i, j) edit distance
    for x1...i, y1...j

want to know E(m, n)
edit dist. for x, y

d = 0 if x_3  y_2
d = 1 if x_3 != y_2

E(0, j) = j # delete all j characters | enptyset to y1...j
E(i, 0) = i # delete all i characters | x1...i to emptyset
"""