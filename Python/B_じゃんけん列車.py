import numpy as np
input_line = input()
enji_num = int(input_line.split()[0])
battle_num = int(input_line.split()[1])
table = np.full(enji_num,1,dtype=int)
for i in range(battle_num):
    row = input().split()
    winner = int(row[0])-1
    loser = int(row[1])-1
    table[winner] += table[loser]
    table[loser] = 0
max_num = np.max(table)
indexes = np.argwhere(table == max_num)
for index in indexes:
    print(int(index+1))