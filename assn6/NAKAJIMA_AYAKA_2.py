
from maze import G 
import networkx 
INF = 10**18

def bfs_shortest_path(G, s, t):
    """
    Input: Graph G = (V, E), directed or undirected; vertec s in V
    Output For all vertices u reachable from s, dist(u) is set to the distancefrom s to u.

    for all u in V:
        dist[u] = infinity
    dit(s) = 0
    Q = [s] (queue containting just s)
    while Q is not empty:
        u = eject(Q)
        for all edges (u, v) in E:
            if dist[v] == infinity:
                inject(Q, v)
                dist[v] = dist[u] + 1
    """
    dist   = {u: INF for u in G.nodes}
    parent = {u: None for u in G.nodes}
    Q = [s]
    dist[s] = 0

    while Q:
        u = Q.pop(0)  # eject
        if u == t:    
            break
        for v in G.adj[u]:
            if dist[v] == INF:
                dist[v] = dist[u] + 1
                parent[v] = u
                Q.append(v)  # inject

    path = []
    cur = t
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return dist, parent, path


if __name__ == "__main__":
    s, t = (0, 0), (29, 24)
    dist, parent, path = bfs_shortest_path(G, s, t)

    if path:
        print("length =", dist[t])       
        print("path_len =", len(path))   
        print("path_head =", path[:10]) 
        print("path_tail =", path[-10:]) 
    else:
        print("No path found")

