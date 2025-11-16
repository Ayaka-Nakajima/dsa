from collections import deque
import networkx as nx

def is_bipartite(G: nx.Graph):
    """
    Solve the following version of Problem 3.7 (a) from the textbook: 
    A bipartite graph is a graph G = (V, E) whose vertices can be partitioned into two sets (V = V1 ∪ V2 and V1 ∩ V2 = ∅) 
    such that
    there are no edges between vertices in the same set (for instance, if u, v ∈ V1, then there is no edge between u
    and v). 
    Give a linear-time algorithm (i. e., in O(|V | + |E|)) to determine whether an undirected graph is bipartite.
    State your algorithm as pseudo-code. Prove that it is correct and that it does indeed run in linear time
    """
    """
    pseudo-code:
    IS-BIPARTITE(G = (V, E)):
    for v in V:
        color[v] ← UNCOLORED

    for s in V:
        if color[s] = UNCOLORED:
            color[s] ← 0
            enqueue(Q, s)
            while Q not empty:
                u ← dequeue(Q)
                for each neighbor w of u:
                    if color[w] = UNCOLORED:
                        color[w] ← 1 - color[u]
                        enqueue(Q, w)
                    else if color[w] = color[u]:
                        return (FALSE, "not bipartite")

    return (TRUE, partition V0={v | color[v]=0}, V1={v | color[v]=1})

    """
    UNCOLORED = -1
    color = {v: UNCOLORED for v in G.nodes()}
    V0, V1 = set(), set()

    for s in sorted(G.nodes()): #O(|V|)
        if color[s] == UNCOLORED:
            color[s] = 0
            V0.add(s)
            Q = deque([s])

            while Q: #O(|V|) in total
                u = Q.popleft()
                for w in sorted(G.neighbors(u)):#O(|E|) in total
                    if color[w] == UNCOLORED:
                        color[w] = 1 - color[u]
                        (V1 if color[w] == 1 else V0).add(w)
                        Q.append(w)
                    elif color[w] == color[u]:
                        return (False, "not bipartite")

    return (True, V0, V1)


