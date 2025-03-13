# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import numpy as np
import sys
input = sys.stdin.read
data = input().splitlines()
N, M = map(int, data[0].split())
table = [list(map(str, line.split())) for line in data[1:]]

combo = np.zeros(M+1,dtype = int)
tag = True
for i in range(M):
    if table[i][0] == table[i][1]:
        if table[i][0] in '#':
            if tag:
                combo[i+1] = combo[i] + 1
                tag = True
            else:
                combo[i+1] = 0
                tag = False
        else:
            combo[i+1] = combo[i] + 1
            tag = True   
    else:
        combo[i+1] = 0
        if table[i][0] in '#':
            tag = False
        else:
            tag = True

print(np.max(combo))