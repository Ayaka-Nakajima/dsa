"""
INPUT: undirected graph G=(V,E), unit edges; nodes u, v
OUTPUT: number of shortest u-to-v paths

BFS-COUNT-SHORTEST(G, u, v):
    for each w in V:
        dist[w] ← infinity
        ways[w] ← 0
    dist[u] ← 0
    ways[u] ← 1

    Q ← empty queue (use list if needed)
    ENQUEUE(Q, u)

    while Q not empty:
        x ← DEQUEUE(Q)
        for each y in Adj[x]:
            if dist[y] = infinity: 
                dist[y] ← dist[x] + 1
                ways[y] ← ways[x]
                ENQUEUE(Q, y)
            else if dist[y] = dist[x] + 1: 
                ways[y] ← ways[y] + ways[x]

    if dist[v] = +infinity:
        return 0
    else:
        return ways[v]

"""
import networkx

def count_shortest_paths(G, u, v):
    INF = 10**18
    dist = {w: INF for w in G.nodes}
    ways = {w: 0   for w in G.nodes}

    dist[u] = 0
    ways[u] = 1
    Q = [u]

    while Q:
        x = Q.pop(0)
        for y in G.adj[x]:
            if dist[y] == INF:
                dist[y] = dist[x] + 1
                ways[y] = ways[x]
                Q.append(y)
            elif dist[y] == dist[x] + 1:
                ways[y] += ways[x]

    return 0 if dist[v] == INF else ways[v]

if __name__ == "__main__":
    G = networkx.Graph()
    G.add_edges_from([
        (1, 2), (1, 3),
        (2, 4), (3, 4),
        (4, 5)
    ])
    u, v = 1, 5
    num_paths = count_shortest_paths(G, u, v)
    ## Expected output: Number of shortest paths from 1 to 5: 2
    print(f"Number of shortest paths from {u} to {v}: {num_paths}")

"""
This program uses Breadth-First Search (BFS) to find both the shortest distance and the number of shortest paths at the same time.
The key idea is that BFS always processes vertices in order of increasing distance from the starting point.

BFS visits each vertex and each edge at most once,
so the time complexity is O(|V| + |E|).


Layers in BFS

When we start BFS from node u, the vertices are grouped into layers by distance:

Distance 0: u (the start)

Distance 1: vertices directly connected to u

Distance 2: vertices that can be reached in two steps
…and so on.

In this way, BFS divides the graph into layers 0, 1, 2,… according to distance.
Every edge connects vertices that are either in the same layer or in two neighboring layers.
Therefore, a shortest path must always go through the layers in order — 0 → 1 → 2 → …

To count how many shortest paths there are, the program keeps a value ways[w] for each vertex w.
This number represents how many shortest paths lead from u to w.

At the start, ways[u] = 1, because there is exactly one way to be at the starting node.

During BFS, when the program looks at a neighbor y of the current vertex x:

If y has not been visited yet (dist[y] == INF), this is the first time we found the shortest distance to y.
So we set dist[y] = dist[x] + 1 and copy the count: ways[y] = ways[x].

If y has already been found with the same distance (dist[y] == dist[x] + 1),
that means there is another shortest path to y, so we add the count: ways[y] += ways[x].

By doing this, every vertex collects the total number of shortest paths that reach it from the previous layer.
Every shortest path to a vertex w must come from one of the vertices x in the previous layer (distance − 1).
The program visits each such x exactly once and adds ways[x] to ways[w].
As a result, after BFS finishes, ways[w] equals the sum of all shortest paths from u to w.

Finally, ways[v] gives the total number of shortest paths from u to v.
If v was never reached (dist[v] stayed infinite), the function correctly returns 0.
"""