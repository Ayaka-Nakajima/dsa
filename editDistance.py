"""
Edit distance(2D)
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


3D
In G = (V, E), L(E -> R)
initial values: if (i, j) dist(i, j, 0) = L(i, j)  in E 
                else if  0 i = j 
                else infinity

update dist(i, j, k) = min( dist(i, j, k-1), dist(i, k, k-1) + dist(k, j, k-1) )
dist(i, j, k) = shortest dist from i to j where the maximal intermediate node is k

"""