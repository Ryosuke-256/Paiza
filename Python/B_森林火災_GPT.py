from collections import deque

# 入力
H, W, R, C, T = map(int, input().split())
R -= 1  # 0-indexに変換
C -= 1

forest = [list(input()) for _ in range(H)]

# 各マスの状態管理（-1: 未訪問, 0〜T: 火が着いた時刻）
burn_time = [[-1]*W for _ in range(H)]

# BFS 初期化
q = deque()
if forest[R][C] == '#':
    q.append((R, C))
    burn_time[R][C] = 0
    forest[R][C] = 'B'  # 火がついた

# 移動方向: 上下左右
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# BFSで火を広げる
while q:
    x, y = q.popleft()
    time_now = burn_time[x][y]

    if time_now >= T:
        continue

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W:
            if forest[nx][ny] == '#' and burn_time[nx][ny] == -1:
                burn_time[nx][ny] = time_now + 1
                forest[nx][ny] = 'B'
                q.append((nx, ny))

# 時刻TになったらB→Aに置き換え
for i in range(H):
    for j in range(W):
        if burn_time[i][j] != -1 and burn_time[i][j] < T:
            forest[i][j] = 'A'
        elif burn_time[i][j] == T:
            forest[i][j] = 'B'

# 出力
for row in forest:
    print(''.join(row))
