
import networkx as nx
from kuruskals_algo import dfs


NODES = list("ABCDEFGHIJKL")

EDGES_FIG36 = [
    #3.6(a)
    # Component 1:
    ("A","B"), ("A","E"), ("E","I"), ("I","J"), ("E","J"),
    # Component 2:
    ("C","D"),  ("D","H"), ("H","L"), ("H","G"), ("G", "K"), ("H","K"),  ("C","G"), ("C", "H"),
    # Component 3: single vertex F (no edges)
    # No edges for F
]

def build_graph():
    G = nx.Graph()
    G.add_nodes_from(NODES)
    G.add_edges_from(EDGES_FIG36)
    return G

#3.6(b) expected results
EXPECTED_PRE = {
    # Component 1:
    "A": 1, "B": 2, "E": 4, "I": 5, "J": 6, 
    # Component 2:
    "C": 11, "D": 12, "H": 13, "G": 14, "K": 15, "L": 18, 
    # Component 3:
    "F": 23
}
EXPECTED_POST = {
    # Component 1:
    "B": 3, "J": 7, "I": 8, "E": 9,  "A": 10,  
    # Component 2:
    "K": 16, "G": 17, "L": 19, "H": 20, "D": 21, "C": 22, 
    # Component 3:
    "F": 24
}
EXPECTED_CC = {
    # Component 1:
    "A": 1, "B": 1, "E": 1, "I": 1, "J": 1,
    # Component 2:
    "C": 2, "D": 2, "G": 2, "H": 2, "K": 2, "L": 2,
    # Component 3:
    "F": 3,
    
}

def main():
    G = build_graph()
    pre, post, cc = dfs(G)
    print("Nodes:", " ".join(NODES))
    print("pre:", pre)
    print("post:", post)
    print("ccnum:", cc)

    # Optional strict checks (activate when EXPECTED_* is filled):
    if EXPECTED_PRE and EXPECTED_POST and EXPECTED_CC:
        assert pre == EXPECTED_PRE, f"pre mismatch:\n expected {EXPECTED_PRE}\n got {pre}"
        assert post == EXPECTED_POST, f"post mismatch:\n expected {EXPECTED_POST}\n got {post}"
        assert cc == EXPECTED_CC, f"ccnum mismatch:\n expected {EXPECTED_CC}\n got {cc}"
        print("\nAll assertions passed for Figure 3.6(b) numbers.")
    else:
        print("\n(Info) EXPECTED_* dicts are empty.")

if __name__ == "__main__":
    main()