import math
"""
Implement a rundimentary spell-checker based on the edit distance algorithm from Chapter 6 of the textbook.
    (a) Implement the edit distance algorithm from the textbook as a function
        edit_distance(word1, word2)
        output (dist, table)
        where dist is the edit distance between the two strings and table is the table E from the textbook.
        (More precisely, table is a list of lists such that table[i][j] = E(i, j) for all i, j.)
    (c) Write a function suggestions(word) which has a single string as input and which reutrns a list of all entries wordlist.txt which have a minimal edit distance from word.
        For example, if the word is "catt" (i.e., a misspelling of "cat"), then the function should return alist with the words “cant”, “cart”, “cast”, “cat”, “cats”, “matt”, and “watt”.
        If the word is "cat"(i.e., a correct spelling), then the function should return a list which contains just "cat".
"""

def edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    E = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        E[i][0] = i
    for j in range(n + 1):
        E[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            cost_sub = E[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1)
            cost_ins = E[i][j - 1] + 1
            cost_del = E[i - 1][j] + 1

            E[i][j] = min(cost_sub, cost_ins, cost_del)

    return E[m][n], E


def load_wordlist(filename="wordlist.txt"):
    with open(filename, "r") as f:
        words = [w.strip() for w in f.readlines()]
    return words

def suggestions(word):
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

# if __name__ == "__main__":
#     test_word = "catt"
#     print(f"Suggestions for '{test_word}':", suggestions(test_word))