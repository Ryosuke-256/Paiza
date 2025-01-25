import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

def max_score(h, w, scores):
    directions = [(-1, 0), (-1, -1), (-1, 1)]  # 上、左上、右上

    #最後の列からスタートしてどんどん上に上がっていくdfs
    @lru_cache(None)
    def dfs(x, y):
        if x == 0:  # 最上段に到達
            return scores[x][y]

        max_points = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                max_points = max(max_points, dfs(nx, ny))

        return scores[x][y] + max_points

    #各列に対して行う
    max_result = 0
    for start_col in range(w):
        max_result = max(max_result, dfs(h - 1, start_col))

    return max_result


input = sys.stdin.read
data = input().splitlines()

h, w = map(int, data[0].split())
scores = [list(map(int, line.split())) for line in data[1:]]

print(max_score(h, w, scores))
