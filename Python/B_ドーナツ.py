import numpy as np
input_line = input()
row_num = int(input_line.split()[0])
col_num = int(input_line.split()[1])
image = np.empty((row_num,col_num),dtype=int)
for i in range(row_num):
    row = input()
    char_list = list(row)
    convertd_list = [1 if char == '.' else 0 if char =='#' else char for char in char_list]
    image[i] = convertd_list
count = 0
for i in range(col_num-2):
    for j in range(row_num-2):
        if image[j,i]+image[j,i+1]+image[j,i+2] == 0:
            judge1 = image[j+1,i]+image[j+1,i+2]
            jduge2 = image[j+1,i+1]
            if (judge1 == 0) and (jduge2 ==1):
                judge3 = image[j+2,i]+image[j+2,i+1]+image[j+2,i+2]
                if judge3 == 0:
                    count += 1

print(count)