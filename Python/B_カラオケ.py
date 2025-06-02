import numpy as np

row, col = map(int, input().split())
table = np.zeros((row + 1, col), dtype=int)

for i in range(row+1):
    for j in range(col):
        table[i,j] = input()

def makescore(C_arr, J_arr):
    score = 100
    for i in range(len(C_arr)):
        judge = abs(C_arr[i] - J_arr[i])
        if judge <= 5:
            score -= 0
        elif judge <= 10:
            score -= 1
        elif judge <= 20:
            score -= 2
        elif judge <= 30:
            score -= 3
        else:
            score -= 5
    return score

score_arr = np.zeros(row, dtype=int)

for i in range(row):
    score_arr[i] = makescore(table[0], table[i + 1])

print(max(max(score_arr),0))