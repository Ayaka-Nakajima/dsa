import networkx
from dfs import dfs # please make sure dfs.py is in the same directory
""" proceduere dag-shortest-paths(G, l, s) 
Input: Dag G = (V, E), edge lengths {l_e: e in E}, vertex s in V 
Output : for all vertices u reachable from s, dist(u) is set to the distance from s to u. 
for all u in V: 
    dist(u) = infinity 
    prev(u) = nil 
dist(s) = 0 
Linerarize G 
for each u in V, in linearized order: 
    for all edges (u, v) in E: 
        update(u, v) 
"""
# moderncomputeralgebra.py
G = networkx.DiGraph()
G.add_nodes_from(range(1, 25))

G.add_edge(2, 3)
G.add_edge(2, 8)
G.add_edge(3, 4)
G.add_edge(4, 7)
G.add_edge(4, 18)
G.add_edge(4, 5)
G.add_edge(4, 12)
G.add_edge(8, 9)
G.add_edge(8, 12)
G.add_edge(8, 13)
G.add_edge(5, 6)
G.add_edge(5, 10)
G.add_edge(9, 10)
G.add_edge(9, 11)
G.add_edge(6, 11)
G.add_edge(6, 22)
G.add_edge(6, 23)
G.add_edge(10, 14)
G.add_edge(12, 14)
G.add_edge(11, 14)
G.add_edge(14, 15)
G.add_edge(14, 18)
G.add_edge(18, 19)
G.add_edge(15, 16)
G.add_edge(15, 23)
G.add_edge(15, 22)
G.add_edge(21, 24)
G.add_edge(19, 20)
G.add_edge(16, 17)
G.add_edge(23, 24)

# Find all ancestors of node 14
def reverse_adj(graph):
    R = {u: set() for u in graph.nodes}
    for u in graph.nodes:
        for v in graph.adj[u]:
            R[v].add(u)
    return R

def ancestors_of(graph, target):
    R = reverse_adj(graph)
    need = set()
    stack = [target]
    while stack:
        v = stack.pop()
        for p in R[v]:
            if p not in need:
                need.add(p)
                stack.append(p)
    return need

need = ancestors_of(G, 14)
need_with_14 = need | {14}

H = networkx.DiGraph()
H.add_nodes_from(need_with_14)
for u in need_with_14:
    for v in G.adj[u]:
        if v in need_with_14:
            H.add_edge(u, v)

pre, post, ccnum = dfs(H)
topo_order = sorted(H.nodes(), key=lambda u: post[u], reverse=True)

print("chapter before chapter14 (ancestor + 14):", sorted(need_with_14))
print("topological order:", topo_order)