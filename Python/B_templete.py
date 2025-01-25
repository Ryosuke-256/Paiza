import numpy as np
row,col = map(int, input().split())
table = np.zeros((row,col),dtype=int)
for i in range(row):
    onerow = map(int,input().split())
    table[i] = onerow



import sys
input = sys.stdin.read
data = input().splitlines()
row_num, col_num = map(int, data[0].split())
table = [list(map(int, line.split())) for line in data[1:]]



