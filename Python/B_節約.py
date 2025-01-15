import numpy as np
input_line = input()
row_num = int(input_line.split()[0])
col_num = int(input_line.split()[1])
table = np.zeros((row_num,col_num),dtype=int)
for i in range(row_num):
    row = input()
    char_list = [int(char) for char in row.split()]
    table[i] = char_list
gonestrore = np.zeros(row_num)
for i in range(col_num):
    col = table[:,i]
    min_idx = np.argmin(col)
    gonestrore[min_idx] += 1
counts = np.sum(gonestrore>0)
print(int(counts))