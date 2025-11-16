import time
import networkx as nx
from NAKAJIMA_AYAKA_3 import is_bipartite

def run_case(name, G, expect_bipartite=True):
    V = G.number_of_nodes()
    E = G.number_of_edges()
    t0 = time.perf_counter()
    ok, *_rest = is_bipartite(G)
    t1 = time.perf_counter()
    assert ok == expect_bipartite, f"[{name}] expected bipartite={expect_bipartite}, got {ok}"
    elapsed = t1 - t0
    work = V + E
    print(f"{name:20s} | V={V:7d}  E={E:7d}  t={elapsed:8.4f}s  t/(V+E)={elapsed/max(work,1):.3e}")

if __name__ == "__main__":
    print("performance test cases for is_bipartite(G) to prove O(|V|+|E|) time complexity")
    print("\n PATH graphs (always bipartite) ")
    for n in [1_000, 2_000, 4_000, 8_000, 16_000]:
        G = nx.path_graph(n)
        run_case(f"path(n={n})", G, expect_bipartite=True)

    print("\n EVEN CYCLE graphs (bipartite) ")
    for n in [1_000, 2_000, 4_000, 8_000, 16_000]:
        G = nx.cycle_graph(n if n % 2 == 0 else n + 1)
        run_case(f"cycle_even(n={n})", G, expect_bipartite=True)

    print("\n ODD CYCLE graphs (not bipartite)")
    for n in [999, 1999, 3999, 7999, 15999]:
        G = nx.cycle_graph(n if n % 2 == 1 else n + 1)
        run_case(f"cycle_odd(n={n})", G, expect_bipartite=False)

    print("\nGRID graphs (bipartite)")
    for (r, c) in [(25, 40), (35, 60), (50, 80), (70, 110)]:
        G = nx.grid_2d_graph(r, c)
        run_case(f"grid({r}x{c})", G, expect_bipartite=True)

    print("\nMIXED graphs (non-bipartite)")
    for k in [2000, 4000, 8000]:
        G = nx.Graph()
        start = 0
        # add several bipartite path components
        for _ in range(4):
            n = k // 4
            H = nx.path_graph(range(start, start + n))
            G.add_nodes_from(H.nodes())
            G.add_edges_from(H.edges())
            start += n
        # add one odd cycle
        odd_cycle_nodes = list(range(start, start + 101))
        for i in range(len(odd_cycle_nodes)):
            u = odd_cycle_nodes[i]
            v = odd_cycle_nodes[(i + 1) % len(odd_cycle_nodes)]
            G.add_edge(u, v)
        run_case(f"mixed_total≈{G.number_of_nodes()}", G, expect_bipartite=False)

    print("\ncode logic check/test cases:" )

    # code logic check/test 1: bipartite 
    G1 = nx.Graph()
    G1.add_edges_from([
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D")
    ])
    result1 = is_bipartite(G1)
    print("Graph 1 (square):", result1)

    # code logic check/test 2: not bipartite-triangle
    G2 = nx.Graph()
    G2.add_edges_from([
        ("A", "B"),
        ("B", "C"),
        ("C", "A")
    ])
    result2 = is_bipartite(G2)
    print("Graph 2 (triangle):", result2)

    # code logic check/test3: non-bipartite-mixed
    G3 = nx.Graph()
    G3.add_edges_from([
        (1, 2), (2, 3),  
        (4, 5), (5, 6), (6, 4)  
    ])
    result3 = is_bipartite(G3)
    print("Graph 3 (mixed):", result3)