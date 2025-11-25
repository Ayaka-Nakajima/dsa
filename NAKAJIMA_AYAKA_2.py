import math

# ----------------------------------------------------------
# Edit Distance (Chapter 6)
# ----------------------------------------------------------
def edit_distance(word1, word2):
    """
    教科書の edit distance アルゴリズム（p.174–177）を忠実に再現。
    E(i, j) は word1[0:i] と word2[0:j] の編集距離。
    戻り値: (distance, table)
    """
    m = len(word1)
    n = len(word2)

    # E テーブル作成 (m+1) x (n+1)
    E = [[0] * (n + 1) for _ in range(m + 1)]

    # 基底条件：1文字ずつ削除 or 挿入
    for i in range(m + 1):
        E[i][0] = i
    for j in range(n + 1):
        E[0][j] = j

    # DP 本体（教科書どおり）
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            cost_sub = E[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1)
            cost_ins = E[i][j - 1] + 1
            cost_del = E[i - 1][j] + 1

            E[i][j] = min(cost_sub, cost_ins, cost_del)

    return E[m][n], E


# ----------------------------------------------------------
# Load word list
# ----------------------------------------------------------
def load_wordlist(filename="wordlist.txt"):
    with open(filename, "r") as f:
        words = [w.strip() for w in f.readlines()]
    return words


# ----------------------------------------------------------
# suggestions(word)
# ----------------------------------------------------------
def suggestions(word):
    """
    word と最小編集距離の単語をすべて返す
    """
    words = load_wordlist()

    best_dist = math.inf
    best_words = []

    for w in words:
        dist, _ = edit_distance(word, w)

        if dist < best_dist:
            best_dist = dist
            best_words = [w]
        elif dist == best_dist:
            best_words.append(w)

    return best_words
