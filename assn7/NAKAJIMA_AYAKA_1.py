'''
idea: always takes cheapest edge. s.t. we do not get a cycle.

procedure kruskal(G, w)
Input: A connected undirected graph G = (V, E) with edge weights w_e
Output: A minimum spanning tree defined by th eedges X
for all u in V: #for each node v of G
    makeset(u)
X = {} #T = (V, empty set)
Sort the edges E by weight
for all edges {u, v} in E, in increasing orderof weight:
#for each edge e in G sorted by weight e = {u, v}
    if find(u) != find(v):#u, v in defferent sets
        add edge {u, v} to X
        union(u, v)#join sets for u, v

#return T
'''

'''

pi(X)... parent of X in tree/set representation
rank(x)... how many levels of nodes point to X
makeset(x): pi(x) = x; rank(x) = 0
find(x): while pi(x) != x: x = pi(x); return x

union(x, y): 
    r_x = find(x); r_y = find(y); 
    if rank(r_x) > rank(r_y):
        pi(r_y) = r_x
    else if rank(r_x) < rank(r_y):
        pi(r_x) = r_y
    else: #rank(r_x) == rank(r_y)
        pi(r_y) = r_x #which one points to which does not matter
        rank(r_x) = rank(r_x) + 1
'''
import networkx as nx

class DisjointSets:
    def __init__(self, elements):# makeset
        self.parent = {x: x for x in elements} #pi(x) = x
        self.rank = {x: 0 for x in elements} #rank(x) = 0

    def find(self, x):#find(x)
        if self.parent[x] != x:# while pi(x) != x:
            self.parent[x] = self.find(self.parent[x])#x = pi(x)
        return self.parent[x]# return x

    def union(self, x, y):#union(x, y)
        rx, ry = self.find(x), self.find(y)# r_x = find(x); r_y = find(y);
        if rx == ry:#avoid cycles
            return False
        if self.rank[rx] < self.rank[ry]:# if rank(r_x) < rank(r_y):
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:# else if rank(r_x) > rank(r_y):
            self.parent[ry] = rx
        else:# else: #rank(r_x) == rank(r_y)
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

def kruskal(G, w): #prosedure kruskal(G, w)
    T = nx.Graph() # X= {} T = (V, ∅)
    for v in G.nodes:
        T.add_node(v) 

    ds = DisjointSets(G.nodes) # for all u in V: makeset(u)

    # sort the edges E by weight
    edges_sorted = sorted(G.edges, key=lambda e: w(e))

    #for edges {u, v} in E, in increasing order of weight:
    for (u, v) in edges_sorted:
        if ds.find(u) != ds.find(v): #if find(u) != find(v):
            T.add_edge(u, v, weight=w((u, v))) #add edge {u, v} to X
            ds.union(u, v) #union(u, v)
    return T

