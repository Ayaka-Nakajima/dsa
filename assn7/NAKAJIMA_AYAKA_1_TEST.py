import networkx as nx
from NAKAJIMA_AYAKA_1 import kruskal

def w_of(G):
    return lambda e: G.edges[e]['weight']

def mst_cost(T):
    return sum(d['weight'] for *_, d in T.edges(data=True))

def is_valid_tree(T, n_expected):
    # A valid spanning tree has n-1 edges and is connected & acyclic
    return T.number_of_nodes()==n_expected and T.number_of_edges()==n_expected-1 and nx.is_tree(T)

def run_case(build_graph_fn, expected_cost, name, check_edges=None):
    G = build_graph_fn()
    T = kruskal(G, w_of(G))
    ok_cost = abs(mst_cost(T) - expected_cost) < 1e-9
    ok_tree = is_valid_tree(T, G.number_of_nodes())
    ok_edges = True
    if check_edges is not None:
        # compare undirected edge sets (ignore order)
        norm = lambda E: {tuple(sorted(e)) for e in E}
        ok_edges = norm(T.edges) == norm(check_edges)
    status = "PASS" if (ok_cost and ok_tree and ok_edges) else "FAIL"
    print(f"[{status}] {name}: cost={mst_cost(T)} expected={expected_cost} edges={T.number_of_edges()}")
    if not ok_cost:  print("  - cost mismatch")
    if not ok_tree:  print("  - not a valid spanning tree")
    if not ok_edges: print("  - edge set mismatch")

# testcases
def case1_triangle():
    # 1) Triangle (unique MST)
    G = nx.Graph()
    G.add_edge(1,2, weight=1)
    G.add_edge(2,3, weight=2)
    G.add_edge(1,3, weight=3)
    return G
# expected MST cost = 1 + 2 = 3

def case2_cycle4_equal():
    # 2) 4-cycle all weights 1 (ties; many MSTs)
    G = nx.Graph()
    edges = [(1,2,1),(2,3,1),(3,4,1),(4,1,1)]
    for u,v,w in edges: G.add_edge(u,v,weight=w)
    return G
# expected cost = 3

def case3_k4_diagonals_light():
    # 3) K4 where diagonals are light
    G = nx.Graph()
    # square sides weight 2
    sides = [("a","b",2),("b","c",2),("c","d",2),("d","a",2)]
    # diagonals weight 1
    diags = [("a","c",1),("b","d",1)]
    for u,v,w in sides+diags: G.add_edge(u,v,weight=w)
    return G
# expected cost = 1 + 1 + 2 = 4

def case4_path5():
    # 4) Path of length 4 (already a tree)
    G = nx.Graph()
    edges = [(1,2,1),(2,3,2),(3,4,3),(4,5,4)]
    for u,v,w in edges: G.add_edge(u,v,weight=w)
    return G
# expected cost = 1+2+3+4 = 10

def case5_star_center0():
    # 5) Star (center 0)
    G = nx.Graph()
    edges = [(0,1,5),(0,2,1),(0,3,3),(0,4,2)]
    for u,v,w in edges: G.add_edge(u,v,weight=w)
    return G
# expected cost = 5+1+3+2 = 11

def case6_negative_edges():
    # 6) Negative edges allowed
    G = nx.Graph()
    edges = [("a","b",-2),("b","c",-1),("c","d",4),("a","d",3),("b","d",2)]
    for u,v,w in edges: G.add_edge(u,v,weight=w)
    return G
# expected MST cost = -2 + -1 + 2 = -1

def case7_two_triangles_bridge():
    # 7) two dense triples + heavy bridge
    G = nx.Graph()
    # triangle 1
    t1 = [(1,2,1),(2,3,1),(1,3,2)]
    # triangle 2
    t2 = [(4,5,1),(5,6,1),(4,6,2)]
    # bridge
    bridge = [(3,4,5)]
    for u,v,w in t1+t2+bridge: G.add_edge(u,v,weight=w)
    return G
# expected cost = (1+1) + (1+1) + 5 = 9

def case8_k5_all_ones():
    # 8) K5 all weights 1 (many MSTs; check only cost)
    G = nx.Graph()
    nodes = [1,2,3,4,5]
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            G.add_edge(nodes[i], nodes[j], weight=1)
    return G
# expected cost = 4

def case9_floats():
    # 9) Floating-point weights
    G = nx.Graph()
    edges = [("p","q",0.1),("q","r",0.2),("r","s",0.3),("p","s",1.0),("p","r",0.9)]
    for u,v,w in edges: G.add_edge(u,v,weight=w)
    return G
# expected cost = 0.1 + 0.2 + 0.3 = 0.6

def case10_square_heavy_diag():
    # 10) square with one heavy diagonal; MST should exclude the heavy one
    G = nx.Graph()
    edges = [("a","b",1),("b","c",1),("c","d",1),("d","a",1),("a","c",10)]
    for u,v,w in edges: G.add_edge(u,v,weight=w)
    return G
# expected cost = 1 + 1 + 1 = 3
# one valid MST edge set (not unique): {ab, bc, cd} or {ab, ad, cd}, etc.

def main():
    run_case(case1_triangle,           3,    "Case1: Triangle (unique)")
    run_case(case2_cycle4_equal,       3,    "Case2: 4-cycle equal weights")
    run_case(case3_k4_diagonals_light, 4,    "Case3: K4 with light diagonals")
    run_case(case4_path5,              10,   "Case4: Path(5)")
    run_case(case5_star_center0,       11,   "Case5: Star center 0")
    run_case(case6_negative_edges,     -1,   "Case6: Negative edges")
    run_case(case7_two_triangles_bridge,9,    "Case7: Two triangles + bridge")
    run_case(case8_k5_all_ones,        4,    "Case8: K5 all ones")
    run_case(case9_floats,             0.6,  "Case9: Floating weights")
    run_case(case10_square_heavy_diag, 3,    "Case10: Square heavy diag")

if __name__ == "__main__":
    main()