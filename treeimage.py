# NAKAJIMA_AYAKA_3_DRAW_TREE.py
# Huffman 木を「上が根・下が葉」の木構造で描画して PNG 保存するスクリプト
# ※提出用ではなくローカル確認用です

import networkx as nx
import matplotlib.pyplot as plt

from NAKAJIMA_AYAKA_3 import tree_of_codes
from huffmandecode import codes  # 教授のファイル


def build_graph_and_positions(tree):
    """
    タプル木 (left, right) から networkx.DiGraph と
    各ノードの座標・ラベル・エッジラベルを作る。

    返り値: (G, pos, node_labels, edge_labels)
    """
    G = nx.DiGraph()
    pos = {}
    node_labels = {}
    edge_labels = {}

    node_id_counter = [0]  # ノードID用カウンタ
    leaf_x = [0]           # 葉の x 座標カウンタ（左から 0,1,2,...）

    def helper(node, depth):
        """
        再帰的に部分木をたどりながらグラフ・座標を作る。

        戻り値: (node_id, xmin, xmax)
          - node_id: この部分木の根ノードID
          - xmin, xmax: この部分木が占める x 範囲
        """
        node_id = node_id_counter[0]
        node_id_counter[0] += 1

        # 葉ノード（文字）
        if isinstance(node, str):
            x = leaf_x[0]
            leaf_x[0] += 1
            y = -depth

            G.add_node(node_id)
            node_labels[node_id] = node
            pos[node_id] = (x, y)

            return node_id, x, x

        # 内部ノード
        left, right = node

        children_info = []

        # 左の子（ビット 0）
        if left is not None:
            left_id, left_xmin, left_xmax = helper(left, depth + 1)
            children_info.append(("0", left_id, left_xmin, left_xmax))

        # 右の子（ビット 1）
        if right is not None:
            right_id, right_xmin, right_xmax = helper(right, depth + 1)
            children_info.append(("1", right_id, right_xmin, right_xmax))

        # 子どもたちの中心あたりに自分を置く
        xs_center = []
        for _, _, xmin, xmax in children_info:
            xs_center.append((xmin + xmax) / 2)

        x = sum(xs_center) / len(xs_center)
        y = -depth

        G.add_node(node_id)
        node_labels[node_id] = "*"  # 内部ノードのラベル

        pos[node_id] = (x, y)

        # エッジ追加（ビットラベルも保存）
        for bit, child_id, xmin, xmax in children_info:
            G.add_edge(node_id, child_id)
            edge_labels[(node_id, child_id)] = bit

        # この部分木全体の x 範囲（左端の子〜右端の子）
        xmin = children_info[0][2]
        xmax = children_info[-1][3]

        return node_id, xmin, xmax

    helper(tree, depth=0)
    return G, pos, node_labels, edge_labels


def main():
    # 1. Huffman 木を構築
    tree = tree_of_codes(codes)

    # 2. グラフとレイアウト情報を作る
    G, pos, node_labels, edge_labels = build_graph_and_positions(tree)

    # 3. 描画
    plt.figure(figsize=(16, 10))  # 木が大きいので少し広めに

    nx.draw(
        G,
        pos,
        labels=node_labels,
        with_labels=True,
        arrows=False,
        node_size=800,
        font_size=8,
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    plt.tight_layout()
    plt.savefig("huffman_tree_topdown.png", dpi=300)
    print("Saved as huffman_tree_topdown.png")


if __name__ == "__main__":
    main()
