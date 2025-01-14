import numpy as np
input_line = input()
row_num = int(input_line.split()[0])
col_num = int(input_line.split()[1])
table = np.zeros((row_num,col_num),dtype=int)
for i in range(row_num):
    row = input()
    char_list = [int(char) for char in row.split()]
    table[i] = char_list
idou = int(input())
ryoukin = 0
now = [0,0]
for i in range(idou):
    row = input()
    train = int(row.split()[0])-1
    station = int(row.split()[1])-1
    ryoukin_tmp = abs(table[train,station] - table[train,now[1]])
    now = [train,station]
    ryoukin += ryoukin_tmp
print(ryoukin)