import numpy as np
input_line1 = input()
kaisuu = int(input_line1.split()[0])
syurui = int(input_line1.split()[1])
input_line2 = input()
row_num = int(input_line2.split()[0])
col_num = int(input_line2.split()[1])
syurui_count = np.zeros(syurui+1)
hatake = np.zeros((row_num,col_num),dtype=int)

data_list = np.zeros((kaisuu,5),dtype=int)
for i in range(kaisuu):
    row = input()
    char_list = row.split()
    data = [int(char) for char in char_list]
    data_list[i] = data
    values = hatake[data[0]-1:data[1],data[2]-1:data[3]]
    
    values_row,values_col = values.shape
    for j in range(values_row):
        for k in range(values_col):
            syurui_count[values[j,k]] += 1
    for row in range(data[0]-1,data[1]):
        for col in range(data[2]-1,data[3]):
            hatake[row,col] = data[4]
            

for i in range(syurui):
    print(int(syurui_count[i+1]))

result = '\n'.join([''.join(str(cell).replace('0', '.') for cell in row) for row in hatake])
print(result)