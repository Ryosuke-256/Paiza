import numpy as np
input_line = input()
edge_num = int(input_line.split()[0])
bingo_num = int(input_line.split()[1])
table = np.zeros((edge_num,edge_num),dtype=int)
for i in range(edge_num):
    row = input()
    char_list = [int(char) for char in row.split()]
    table[i] = char_list
tmp = input()
number_list  = [int(char) for char in tmp.split()]
for i in range(bingo_num):
    number = number_list[i]
    index = np.argwhere(table == number)
    if index.size > 0:
        for idx in index:
            table[idx[0],idx[1]] = 0
bingo_count = 0
for i in range(edge_num):
    tmp = table[i,:]
    if np.all(tmp == 0):
        bingo_count += 1
for i in range(edge_num):
    tmp = table[:,i]
    if np.all(tmp == 0):
        bingo_count += 1
main_diag = np.diag(table)
if np.all(main_diag == 0):
    bingo_count += 1
anti_diag = np.diag(np.fliplr(table))
if np.all(anti_diag == 0):
    bingo_count += 1
print(bingo_count)