import numpy as np
input_line = input()
row_num = int(input_line.split()[0])
col_num = int(input_line.split()[1])
table = np.full((row_num,col_num),'B',dtype=str)
judge = 0
for i in range(row_num):
    row = input()
    choco_list = [int(char) for char in row.split()]
    sugar_sum = sum(choco_list)
    sugar_count = 0
    sugar_idx = 0
    while judge == 0:
        sugar_count += choco_list[sugar_idx]
        if sugar_count < sugar_sum/2:
            table[i,sugar_idx] = 'A'
            sugar_idx += 1
            continue
        elif sugar_count == sugar_sum/2:
            table[i,sugar_idx] = 'A'
            break
        else:
            judge = 1

if judge == 1:
    print('No')
else:
    print('Yes')
    for row in table:
        print(''.join(row))