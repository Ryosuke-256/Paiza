import numpy as np
input_line = input()
row_num = int(input_line.split()[0])
col_num = int(input_line.split()[1])
sum_num = np.zeros(col_num,dtype=int)
count_num = np.zeros(col_num,dtype = int)
def int_try(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    except TypeError:
        return False
        
for i in range(row_num):
    row = input()
    char_list = row.split()
    for j in range(col_num):
        if int_try(char_list[j]):
            tmp1 = int(char_list[j])
            if (tmp1 >= 0) and (tmp1 <=100):
                sum_num[j] += int(tmp1)
                count_num[j] += 1

for i in range(col_num):
    if not(count_num[i] == 0):
        print(int(sum_num[i]/count_num[i]))
    else:
        print(0)