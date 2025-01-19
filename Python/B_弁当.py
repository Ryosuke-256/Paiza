import numpy as np
from itertools import product
input_line = input()
bento_num = int(input_line.split()[0])
calory_limit = int(input_line.split()[1])
table = np.zeros((3,bento_num),dtype=int)
for i in range(3):
    row = input()
    char_list = [int(char) for char in row.split()]
    table[i] = char_list
unique_bento_values = np.unique(table[2])
bento_index_group = [np.where(table[2] == value)[0] for value in unique_bento_values]
all_bento_combination = list(product(*bento_index_group))
shape = np.shape(all_bento_combination)
result_suf = -1
if shape[1] == 3:
    for combination in all_bento_combination:
        total_calory = table[0][combination[0]] + table[0][combination[1]] + table[0][combination[2]]
        total_sufficienct = table[1][combination[0]] + table[1][combination[1]] + table[1][combination[2]]
        if total_calory > calory_limit:
            continue
        if total_sufficienct > result_suf:
            result_suf = total_sufficienct
print(result_suf)