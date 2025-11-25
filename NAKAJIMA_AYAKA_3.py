import networkx as nx
import math


# ----------------------------------------------------------
# Floyd–Warshall (教科書 Chapter 6, p.187)
# ----------------------------------------------------------
def floyd_warshall(G):
    """
    G: networkx Graph
    戻り値: dist[(u, v)] の辞書
    """

    nodes = list(G.nodes())
    dist = {}

    # 初期化
    for u in nodes:
        for v in nodes:
            if u == v:
                dist[(u, v)] = 0
            elif G.has_edge(u, v):
                dist[(u, v)] = 1  # エッジの重みは1（迷路なので無重み）
            else:
                dist[(u, v)] = math.inf

    # 教科書どおりの三重ループ
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]:
                    dist[(i, j)] = dist[(i, k)] + dist[(k, j)]

    return dist


# ----------------------------------------------------------
# 最も遠いノード対を見つける
# ----------------------------------------------------------
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


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def main():
    # Step (a): maze02.gml を読み込む
    G = nx.read_gml("maze02.gml")

    # Step (b): Floyd–Warshall を実行
    dist = floyd_warshall(G)

    # Step (c): 最長距離ノード対
    max_dist, pairs = find_furthest_pairs(dist)

    print("Longest shortest-path distance:", max_dist)
    print("Node pairs with this distance:")
    for u, v in pairs:
        print(f"{u} - {v}")


if __name__ == "__main__":
    main()
