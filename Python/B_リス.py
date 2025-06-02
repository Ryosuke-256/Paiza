import numpy as np
row_n,col_n = map(int, input().split())
N = input()
matrix = np.zeros((row_n,col_n),dtype=int)
for i in range(row_n):
    matrix[i] = list(map(int,input().split()))

table = np.zeros((row_n,col_n,4),dtype=int)
for i in range(row_n):
    for j in range(col_n):
        # 右方向
        table[i, j, 0] = np.sum(matrix[i, j:min(j+N, col_n)])
        # 左方向
        table[i, j, 1] = np.sum(matrix[i, max(j-N+1, 0):j+1])
        # 下方向
        table[i, j, 2] = np.sum(matrix[i:min(i+N, row_n), j])
        # 上方向
        table[i, j, 3] = np.sum(matrix[max(i-N+1, 0):i+1, j])

result = np.max(table)
print(result)
