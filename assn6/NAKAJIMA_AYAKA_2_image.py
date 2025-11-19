import matplotlib.pyplot as plt
from maze import G
from kuruskals_algo import bfs_shortest_path

def draw_maze_with_path(G, path=None, thin_alpha=0.15, lw_maze=0.8, lw_path=2.8):
    # 迷路の全通路（薄い線）
    drawn = set()
    for u in G.nodes:           # adj から無向辺を一度だけ描く
        for v in G.adj[u]:
            if (v, u) in drawn:
                continue
            drawn.add((u, v))
            x = [u[0], v[0]]
            y = [u[1], v[1]]
            plt.plot(x, y, linewidth=lw_maze, alpha=thin_alpha)

    # 最短路（太い線）
    if path and len(path) >= 2:
        xs = [p[0] for p in path]
        ys = [p[1] for p in path]
        plt.plot(xs, ys, linewidth=lw_path)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().invert_yaxis()   # 上下を迷路っぽく
    plt.axis('off')
    plt.tight_layout()

if __name__ == "__main__":
    s, t = (0, 0), (29, 24)
    _, _, path = bfs_shortest_path(G, s, t)
    draw_maze_with_path(G, path)
    plt.savefig("maze_shortest_path.png", dpi=300, bbox_inches="tight")
