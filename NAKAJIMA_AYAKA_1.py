import csv
import math

# -----------------------------
# Load forest tiles
# -----------------------------
def load_forest_tiles(filename="forest.csv"):
    forest = set()
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)# skip header

        for row in reader:
            x, y = map(int, row)
            forest.add((x, y))
    return forest


# -----------------------------
# Euclidean distance
# -----------------------------
def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


# -----------------------------
# Compute subsets S_i for all hut positions
# -----------------------------
def compute_hut_sets(forest):
    sets = []  # list of (location, frozenset)
    for i in range(20):
        for j in range(20):
            hut = (i, j)
            cover = set()
            for f in forest:
                if distance(hut, f) <= 8:
                    cover.add(f)
            if cover:
                sets.append((hut, frozenset(cover)))
    return sets


# -----------------------------
# Greedy Set Cover (Section 5.4, Chapter 5)
# -----------------------------
def greedy_set_cover(universe, sets):
    U = set(universe)
    chosen = []

    while U:
        best_set = None
        best_cover = set()

        for loc, S in sets:
            cover = U & S
            if len(cover) > len(best_cover):
                best_cover = cover
                best_set = (loc, S)

        if best_set is None:
            raise Exception("No remaining set can cover the universe.")

        chosen.append(best_set[0])
        U -= best_cover

    return chosen


# -----------------------------
# Main: Execute algorithm
# -----------------------------
def main():
    forest = load_forest_tiles()
    hut_sets = compute_hut_sets(forest)
    solution = greedy_set_cover(forest, hut_sets)

    print("Woodcutter hut locations (Greedy Set Cover):")
    for loc in solution:
        print(loc)
    print("Total huts needed:", len(solution))


if __name__ == "__main__":
    main()
