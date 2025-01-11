from collections import deque

# BFSによる最短距離計算
def bfs(maze, start, goal, N, M):
    # 4方向の移動（上下左右）
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # キューの初期化
    queue = deque([(start[0], start[1], 0)])  # (行, 列, 移動回数)
    visited = [[False] * M for _ in range(N)]  # 訪問済みのマス
    visited[start[0]][start[1]] = True  # スタート位置を訪問済みに
    
    while queue:
        x, y, dist = queue.popleft()
        
        # ゴールに到達した場合
        if (x, y) == goal:
            return dist
        
        # 上下左右に移動
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 迷路内で、道（'0'）またはゴール（'g'）であれば
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if maze[nx][ny] == '0' or maze[nx][ny] == 'g':
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
    
    # ゴールに到達できない場合
    return "Fail"

def main():
    # 入力の読み込み
    M, N = map(int, input().split())  # 列数と行数
    maze = [input().split() for _ in range(N)]  # 迷路の入力
    
    # スタートとゴールの位置を探す
    start = goal = None
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 's':
                start = (i, j)
            elif maze[i][j] == 'g':
                goal = (i, j)
    
    # BFSで最短距離を求める
    result = bfs(maze, start, goal, N, M)
    
    # 結果を出力
    print(result)

if __name__ == "__main__":
    main()
