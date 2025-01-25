import numpy as np
row,col = map(int, input().split())
table = np.zeros((row,col),dtype=int)
for i in range(row):
    onerow = map(int,input().split())
    table[i] = onerow



