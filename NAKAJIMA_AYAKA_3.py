import networkx as nx
import math


def floyd_warshall(G):
    """
    教科書 Chapter 6 の Floyd–Warshall を
    2次元配列ベースで実装した版。
    戻り値: dist[(u, v)] の辞書
    """
    nodes = list(G.nodes())
    n = len(nodes)

    # ノード → インデックス の対応表
    idx = {node: i for i, node in enumerate(nodes)}

    # dist[i][j] テーブルを作成
    dist = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # エッジの重み（迷路なので全部 1）
    for u, v in G.edges():
        i = idx[u]
        j = idx[v]
        dist[i][j] = 1
        dist[j][i] = 1      # 無向グラフ前提

    # Floyd–Warshall 本体
    for k in range(n):
        for i in range(n):
            dik = dist[i][k]
            if dik == math.inf:
                continue
            for j in range(n):
                new = dik + dist[k][j]
                if new < dist[i][j]:
                    dist[i][j] = new

    # 辞書形式に変換して返す（課題仕様どおり）
    dist_dict = {}
    for i in range(n):
        for j in range(n):
            dist_dict[(nodes[i], nodes[j])] = dist[i][j]

    return dist_dict


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
    # maze02.gml を NAKAJIMA_AYAKA_3.py と同じフォルダに置いておくこと
    G = nx.read_gml("maze02.gml")

    print("nodes:", len(G.nodes()), "edges:", len(G.edges()))

    dist = floyd_warshall(G)
    max_dist, pairs = find_furthest_pairs(dist)

    print("Longest shortest-path distance:", max_dist)
    print("Node pairs with this distance:")
    for u, v in pairs:
        print(f"{u} - {v}")


if __name__ == "__main__":
    main()
