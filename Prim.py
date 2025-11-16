'''
prim(G, w):
    for all nodes V:
        cost(v) = infinity
        prev(v) = null
    pick node s at random
    cost(s) = 0
    H = make priority queue of all nodes with key = cost(v)
    while H != empty:
        pop u from H
        for all nodes adjacent to u:
            cost(x) := min(cost(x), weight(x,u))
            prev := u if dist got smaller    
'''

G.add_edge('a','b', weight=5)
G.add_edge('b','c', weight=2)
G.add_edge('c','d', weight=1)
G.add_edge('d','e', weight=4)
G.add_edge('e','f', weight=2)
G.add_edge('d','f', weight=5)
G.add_edge('a','c', weight=6)
G.add_edge('a','d', weight=4)
G.add_edge('b','d', weight=1)
G.add_edge('c','e', weight=3)
G.add_edge('c','f', weight=3)


