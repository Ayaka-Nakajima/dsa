'''
combine (Tree(f1, e1, r1), Tree(f2, e2, r2)) = Tree(f1 + f2, x, y)
tree= Leaf of (int, char)
        | Node of (int, tree, tree)
for each (char, int) in table:
    put Leaf(int, char)  into priority queue

while queue has at least two entries:
    pop two smallest entries
    combine them into a Tree and add tree to the queue
    return single entry of the queue
'''
# NAKAJIMA_AYAKA_3.py
# Problem 3: Huffman tree construction and decoding

def tree_of_codes(codes):
    """
    codes: dict {character: bitstring}
    return: binary tree as nested tuples, leaves are characters
            e.g. ('a', ('b', 'c'))
    """
    if not codes:
        raise ValueError("codes dictionary must be non-empty")

    # まずは中間表現として dict ベースのトライ木を作る
    # 各ノードは {'0': left_child, '1': right_child} のような辞書。
    # 子はさらに dict（内部ノード）か str（葉）になる。
    root = {}

    for ch, code in codes.items():
        if not isinstance(code, str):
            raise TypeError("Code words must be strings")

        node = root
        for i, bit in enumerate(code):
            if bit not in ("0", "1"):
                raise ValueError("Codes must consist only of '0' and '1'")

            is_last = (i == len(code) - 1)

            if is_last:
                # 最後のビットに対応する子に文字を置く
                child = node.get(bit)

                # 既に内部ノードや別の葉が入っていたら Huffman コードとしてはおかしいが、
                # 問題文では「常に正しい Huffman コード」と保証されているので
                # 厳密なチェックはしなくてもよい。
                node[bit] = ch
            else:
                # 途中のビットなら内部ノード（dict）を下りていく
                child = node.get(bit)
                if child is None or isinstance(child, str):
                    # まだ何もない or 葉がある場合は新しく内部ノードを作る
                    child = {}
                    node[bit] = child
                node = child

    # dict ベースのトライ木を、問題指定の「タプル木」に変換する
    def to_tuple(node_dict):
        # Huffman コードでは各内部ノードに 0/1 のどちらか（もしくは両方）の子がある
        left = node_dict.get("0")
        right = node_dict.get("1")

        if isinstance(left, dict):
            left = to_tuple(left)
        if isinstance(right, dict):
            right = to_tuple(right)

        return (left, right)

    # ルートがただの葉になるケース（1文字だけのコード）も理論的にはありうるので一応考慮
    if isinstance(root, dict):
        return to_tuple(root)
    else:
        # ほぼ来ないはず
        return root


def huffman_decode(string, tree):
    """
    string: bitstring consisting of '0' and '1'
    tree  : binary tree as nested tuples from tree_of_codes
    return: decoded string
    """
    result_chars = []
    node = tree

    for bit in string:
        if bit == "0":
            node = node[0]
        elif bit == "1":
            node = node[1]
        else:
            raise ValueError("Input string must contain only '0' and '1'")

        # 葉（文字）に到達したら出力に追加し、ルートに戻る
        if isinstance(node, str):
            result_chars.append(node)
            node = tree

    # 問題文の前提より、最後は必ずルートに戻っているはず（入力は常に正しい）
    return "".join(result_chars)
