# Problem 1
# Consider the undirected graph G = (V, E)
# with V = {0, ..., 19} and E = {{i, i^2+i+1 mod 20}| i = 0, ...,19}.
# Use Python and the NetworkX library to draw the graph and
# submit the picture togather with the code.
# WHat are the connected components? Is the graph a tree? a forest?
# Answer the questions using the plot or with the functions in the NetworkX library

import networkx as nx
import matplotlib.pyplot as plt

def build_graph():
    n = 20
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        j = (i*i + i + 1) % n
        G.add_edge(i, j)
    return G

if __name__ == "__main__":
    G = build_graph()

    # Draw
    pos = nx.circular_layout(G)
    plt.figure(figsize=(6, 6), dpi=160)
    nx.draw(G, pos, with_labels=True, node_size=600, font_size=8)
    plt.title("Problem 1: Undirected graph on V={0..19} with edges {i, i^2+i+1 mod 20}")
    plt.tight_layout()
    plt.savefig("problem1_graph.png")

    # Connected components
    components = [sorted(list(c)) for c in nx.connected_components(G)]
    components_sorted = sorted(components, key=lambda c: (len(c), c))

    # Tree / forest checks
    is_tree = nx.is_tree(G)
    is_forest = nx.is_forest(G)

    # Print results (no extra input/output beyond what's requested)
    print("Connected components (sorted):")
    for idx, comp in enumerate(components_sorted, 1):
        print(f"  Component {idx}: {comp}")
    print(f"\nIs the graph a tree? {is_tree}")
    print(f"Is the graph a forest? {is_forest}")
