import numpy as np
row_num = int(input())
table_original = np.zeros((row_num,row_num),dtype=int)
table_remove = np.zeros((row_num,row_num),dtype=int)
table_finish = np.zeros((row_num,row_num),dtype=int)
center = (row_num+1)/2-1
for row in range(row_num):
    for col in range(row_num):
        table_finish[row,col] = center+1 - max(abs(center-row),abs(center-col))
for i in range(row_num):
    row = input()
    char_list = [int(char) for char in row.split()]
    table_original[i] = char_list
table_remove = table_original - table_finish
print(sum(sum(table_remove)))