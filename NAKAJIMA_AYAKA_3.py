import networkx as nx
import math
"""
Problem 3 (5 points). Determine which two locations are furthest away from each other in a maze.

(b) Implement the Floyd–Warshall algorithm from Section 6.6 of the textbook as a function with the name
floyd_warshall. It should take a graph as input and return a table of the distances from any node to
any other node. The table should be returned as a dictionary where the keys are pairs of nodes and the
values are the distances.
(c) Find the node pairs which are furthest away from each other and print them. (There could be only one
maximal distance pair or several.)
(d)  In addition, you must also run the program on your computer and submit a screenshot or a
copy of the output. Just the code alone will not receive full marks.
"""

def floyd_warshall(G):

    nodes = list(G.nodes())
    dist = {}
    for u in nodes:
        for v in nodes:
            if u == v:
                dist[(u, v)] = 0
            elif G.has_edge(u, v):
                dist[(u, v)] = 1
            else:
                dist[(u, v)] = math.inf

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]:
                    dist[(i, j)] = dist[(i, k)] + dist[(k, j)]

    return dist


def find_furthest_pairs(dist):
    max_dist = -1
    pairs = []

    for (u, v), d in dist.items():
        if d == math.inf:
            continue
        if d > max_dist:
            max_dist = d
            pairs = [(u, v)]
        elif d == max_dist:
            pairs.append((u, v))

    return max_dist, pairs


def main():
    G = nx.read_gml("maze02.gml")
    dist = floyd_warshall(G)
    max_dist, pairs = find_furthest_pairs(dist)
    print("Longest shortest-path distance:", max_dist)
    print("Node pairs with this distance:")
    for u, v in pairs:
        print(f"{u} - {v}")


if __name__ == "__main__":
    main()
