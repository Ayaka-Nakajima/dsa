import csv
import math
"""
Find optimal locations for resource extractors in a strategy game.
"""

#(b) Load forest tiles from CSV file
def load_forest_tiles(filename="forest.csv"):
    forest = set()
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)# skip header

        for row in reader:
            x, y = map(int, row)
            forest.add((x, y))
    return forest


#(c)
def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


#(a)
def compute_hut_sets(forest):
    sets = []  # list of (location, frozenset)
    #The size is 20x20 tiles.
    for i in range(20):
        for j in range(20):
            hut = (i, j)
            cover = set()
            for f in forest:
                if distance(hut, f) <= 8:# Euclidian distance
                    cover.add(f)
            if cover:
                sets.append((hut, frozenset(cover)))
    return sets


"""
Input: A set of elements B; sets S1, S2, ..., Sm is a subset of B. 
Output: A selection of the Si whose union is B.
Cost: Number of sets picked.

Repeat until all elements B are covered:
    Pick the set Si that covers the largest number of uncovered elements.
"""
#(d) Greedy Set Cover Algorithm
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
