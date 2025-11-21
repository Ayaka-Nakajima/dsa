"""
Problem 2 (5 points). Use Kruskal’s algorithm to detect clusters in a data set.
(a) The data set is on Canvas (in the Files section) under the name clustering.csv. It contains 40
observation with two numerical variables x and y. (Each observation also has a unique ID.)
CIS 3223 Assignment 7
(b) Use the csv or pandas module to read the data and then convert it into a networkx.Graph where the
nodes are the observations, there is an edge between any two nodes, and the weight of an edge is the
Euclidean distance between the pairs of x and y values of the two nodes. (That is, we interprete the
variables as (x, y) coordinates on the Euclidean plane.)
(c) Find a minimum spanning tree for the graph. You can use your own implementation of Kruskal’s or Prim’s
algorithm or a library function.
(d) Inspect the tree and find a good criterion for removing edges so that you get a sensible clustering with at
least three different clusters.
(e) Produce a plot of your clusters using, e. g., the plot function from matplotlib.pyplot. (Other graphics
libraries are also fine.) The plot should show the observations (interpreted as points with (x, y) coordinates
given by the variables) where different clusters use different colours or symbols.
(f) Submit a screenshot of the plot together with a screenshot of your Python session or script. Your screenshot
should contain all parts of the process from loading the data to creating the plot. Add explanations to your
various steps. Only screenshots will be accepted for this problem—do not submit any source code files.
Make sure that the pictures use a sufficient resolution.
Optional: Feel free to experiment with other distances (e. g., Manhattan distance or Chebychev distance) and see if
that changes your clusters.
"""
# LASTNAME_FIRSTNAME_2_SCRIPT.py
# Problem 2: Clustering via Kruskal MST
# (b) load -> (c) MST -> (d) cut criterion -> (e) plot

import csv, math, itertools, sys
import networkx as nx
import matplotlib.pyplot as plt

# ===== (b) データ読み込み -> 完全グラフ作成 =====
# 章対応: 点集合から完全グラフを作り、辺重み=ユークリッド距離（ch.5: MST前提の重み付き無向連結グラフ）[ref]
def load_points(filename):
    pts = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # id は int にしておくと扱いやすい
            pts.append((int(row["id"]), float(row["x"]), float(row["y"])))
    return pts

def build_complete_graph(points):
    G = nx.Graph()
    for pid, x, y in points:
        G.add_node(pid, x=x, y=y)
    for (i, a), (j, b) in itertools.combinations(enumerate(points), 2):
        (id1, x1, y1) = a
        (id2, x2, y2) = b
        w = math.hypot(x1 - x2, y1 - y2)  # Euclidean distance
        G.add_edge(id1, id2, weight=w)
    return G

# ===== (c) 最小全域木 (MST) =====
# ch.5: Kruskalの「重み昇順＋サイクル回避=貪欲選択」。
# networkxの minimum_spanning_tree でもOK（Kruskal/Prim相当）
def mst_kruskal(G):
    # 自前Kruskal（course用のDSU実装）
    class DSU:
        def __init__(self, nodes):
            self.p = {v: v for v in nodes}
            self.r = {v: 0 for v in nodes}
        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb: return False
            if self.r[ra] < self.r[rb]:
                self.p[ra] = rb
            elif self.r[ra] > self.r[rb]:
                self.p[rb] = ra
            else:
                self.p[rb] = ra
                self.r[ra] += 1
            return True

    T = nx.Graph()
    T.add_nodes_from(G.nodes)
    dsu = DSU(G.nodes)

    # 重み昇順に走査（Kruskalの貪欲選択）
    for (u, v) in sorted(G.edges, key=lambda e: G.edges[e]["weight"]):
        if dsu.find(u) != dsu.find(v):
            T.add_edge(u, v, weight=G.edges[u, v]["weight"])
            dsu.union(u, v)
    return T

def mst_cost(T):
    return sum(d["weight"] for *_, d in T.edges(data=True))

# ===== (d) “良い切断基準”でクラスタ化 =====
# 発想: MSTは全点を最小コストで連結する“細い骨組み”。長い辺はクラスター間の“橋”になりがち。
# → MSTの「長い辺」を上位K-1本カットするとKクラスタ（ch.5 のカット性質と整合）。
def cluster_from_mst(T, desired_k=None):
    edges = list(T.edges(data=True))
    # 重みで降順に並べる（長い辺=弱い結合）
    edges_sorted = sorted(edges, key=lambda e: e[2]["weight"], reverse=True)

    if desired_k is None:
        # 自動: “最大ギャップ”で切る（エルボー的）
        ws = [w for _, _, d in edges_sorted for w in [d["weight"]]]
        if len(ws) >= 2:
            diffs = [(i, ws[i] - ws[i+1]) for i in range(len(ws) - 1)]
            idx, _ = max(diffs, key=lambda t: t[1])
            cut_edges = set(tuple(sorted((u, v))) for u, v, _ in edges_sorted[: idx + 1])
        else:
            cut_edges = set()
    else:
        k = max(1, desired_k)
        cut_edges = set(tuple(sorted((u, v))) for u, v, _ in edges_sorted[: max(0, k - 1)])

    # 切断して連結成分をラベル付け
    blocked = cut_edges
    parent = {v: v for v in T.nodes}
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb: parent[rb] = ra

    for u, v in T.edges:
        key = tuple(sorted((u, v)))
        if key in blocked:  # カット対象は張らない
            continue
        union(u, v)

    reps = {v: find(v) for v in T.nodes}
    # 代表→0..C-1に正規化
    uniq = {r: i for i, r in enumerate(sorted(set(reps.values())))}
    labels = {v: uniq[reps[v]] for v in T.nodes}

    return labels, cut_edges

# ===== (e) 可視化（クラスタ色分け） =====
def plot_clusters(G, labels, title="Clusters from MST"):
    xs = [G.nodes[v]["x"] for v in G.nodes]
    ys = [G.nodes[v]["y"] for v in G.nodes]
    cids = [labels[v] for v in G.nodes]
    # カラーマップ簡易
    cmap = plt.get_cmap("tab10")
    colors = [cmap(i % 10) for i in cids]

    plt.figure(figsize=(7, 5))
    plt.scatter(xs, ys, c=colors, s=40, edgecolors="k", linewidths=0.5)
    for v in G.nodes:
        plt.text(G.nodes[v]["x"] + 0.02, G.nodes[v]["y"] + 0.02, str(v), fontsize=8)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.show()

# ===== メイン（実行→スクショ用） =====
if __name__ == "__main__":
    print("== (b) Load dataset ==")
    pts = load_points("clustering.csv")
    print(f"Loaded {len(pts)} points")

    print("== (b) Build complete graph with Euclidean weights ==")
    G = build_complete_graph(pts)
    print(f"Graph |V|={G.number_of_nodes()} |E|={G.number_of_edges()}")

    print("== (c) Compute MST via Kruskal ==")
    T = mst_kruskal(G)
    print(f"MST edges: {T.number_of_edges()}  (should be |V|-1)")
    print(f"MST total cost: {mst_cost(T):.4f}")

    # ---- 3クラスタ以上にしたい: desired_k=3 を指定（課題(d)の条件を満たす） ----
    desired_k = 3  # ここを変えるとクラスタ数も変えられる
    print(f"== (d) Cluster by cutting top-{desired_k-1} longest MST edges ==")
    labels, cut_edges = cluster_from_mst(T, desired_k=desired_k)
    print(f"Cut edges ({len(cut_edges)}): {sorted(cut_edges)}")
    num_clusters = len(set(labels.values()))
    print(f"Clusters found: {num_clusters}")

    print("== (e) Plot clusters ==")
    plot_clusters(G, labels, title=f"Clusters (K={num_clusters}) via Kruskal-MST cut")
    
