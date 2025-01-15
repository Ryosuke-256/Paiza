import numpy as np
input_line = input()
searved_num = int(input_line.split()[0])
row_num = int(input_line.split()[1])
col_num = int(input_line.split()[2])
Best_seat = [int(input_line.split()[3]),int(input_line.split()[4])]
table = np.zeros((row_num,col_num),dtype=int)
for i in range(searved_num):
    row = input()
    researved_seat = [int(char) for char in row.split()]
    table[researved_seat[0],researved_seat[1]] += 1
distance_table = np.full((row_num,col_num),1000)
for row in range(row_num):
    for col in range(col_num):
        if table[row,col] == 0:
            distance = abs(row-Best_seat[0])+abs(col-Best_seat[1])
            distance_table[row,col] = distance
min_dist = np.min(distance_table)
indicies = np.argwhere(distance_table == min_dist)
for i in indicies:
    result = ' '.join(map(str,i))
    print(result)