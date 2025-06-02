import numpy as np
row_all,col_all,row_bigin,col_bigin,time_limit = map(int, input().split())
table_map = np.zeros((row_all,col_all),dtype=str)
for i in range(row_all):
    table_map[i] = list(input())

if table_map[row_bigin-1,col_bigin-1] == '#':
    table_map[row_bigin-1,col_bigin-1] ='B'

def change_tile(table_map,pos_row,pos_col):
    if table_map[pos_row,pos_col] == '#':
        table_map[pos_row,pos_col] = 'B'
    return table_map

time_now = 0
transposition = np.array([[1,0],[-1,0],[0,1],[0,-1]])
while(time_now < time_limit):
    pos_B_row, pos_B_col = np.where(table_map == 'B')
    pos_B_reshaped =list(zip(pos_B_row, pos_B_col))
    for pos_B_tmp in pos_B_reshaped:
        pos_B_tmp = list(pos_B_tmp)
        pos_willburn = [pos_B_tmp+delta for delta in transposition]
        pos_willburn = np.clip(pos_willburn,[0,0],[row_all-1,col_all-1])
        for pos_tmp_willburn_row,pos_tmp_willburn_col in pos_willburn:
            if table_map[pos_tmp_willburn_row,pos_tmp_willburn_col] == '#':
                table_map[pos_tmp_willburn_row,pos_tmp_willburn_col] = 'B'
        table_map[pos_B_tmp[0],pos_B_tmp[1]] = 'A'
    #print(table_map)
    time_now += 1

result = "\n".join("".join(row) for row in table_map)
print(result)
