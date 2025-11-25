import csv
import math
import matplotlib.pyplot as plt

RADIUS = 8.0   # hut のカバー半径
GRID_SIZE = 20 # 20x20 マップ


def load_forest_tiles(filename="forest.csv"):
    forest = []
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        next(reader, None)  # ヘッダ x,y を飛ばす
        for row in reader:
            if not row:
                continue
            x, y = map(int, row)
            forest.append((x, y))
    return forest


def is_covered(tile, huts, radius=RADIUS):
    x, y = tile
    for hx, hy in huts:
        dx = x - hx
        dy = y - hy
        if math.sqrt(dx*dx + dy*dy) <= radius:
            return True
    return False


def main():
    # 森タイル読み込み
    forest = load_forest_tiles()

    # あなたの Greedy 解
    huts = [(8, 14), (7, 4), (12, 7), (0, 7)]

    # カバー状況を判定
    covered = []
    uncovered = []
    for tile in forest:
        if is_covered(tile, huts):
            covered.append(tile)
        else:
            uncovered.append(tile)

    # プロット準備
    plt.figure(figsize=(8, 8))

    # カバーされている森タイル（青の点）
    if covered:
        cx = [x for x, y in covered]
        cy = [y for x, y in covered]
        plt.scatter(cx, cy, c="blue", s=30, label="Covered forest")

    # カバーされていない森タイル（赤バツ）
    if uncovered:
        ux = [x for x, y in uncovered]
        uy = [y for x, y in uncovered]
        plt.scatter(ux, uy, c="red", marker="x", s=60, label="Uncovered forest")

    # hut の位置（黒い四角）
    hx = [x for x, y in huts]
    hy = [y for x, y in huts]
    plt.scatter(hx, hy, c="black", s=80, marker="s", label="Woodcutter huts")

    # hut ごとに半径8の円を描く
    ax = plt.gca()
    for x, y in huts:
        circle = plt.Circle((x, y), RADIUS, fill=False, linestyle="--")
        ax.add_patch(circle)
        plt.text(x + 0.2, y + 0.2, f"({x},{y})", fontsize=9, color="black")

    # 軸やグリッドなど
    plt.xlim(-1, GRID_SIZE)
    plt.ylim(-1, GRID_SIZE)
    plt.gca().invert_yaxis()  # (0,0) を左上っぽく
    plt.xticks(range(GRID_SIZE))
    plt.yticks(range(GRID_SIZE))
    plt.grid(True, linestyle=":")

    plt.title("Forest tiles and coverage by woodcutter huts")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.tight_layout()
    plt.savefig("forest_coverage.png", dpi=300)
    plt.show()

    # 最後に未カバータイルがあるかメッセージ
    if not uncovered:
        print("All forest tiles are covered by the huts. ✅")
    else:
        print("There are uncovered forest tiles. ❌")
        print("Uncovered tiles:", uncovered)


if __name__ == "__main__":
    main()
