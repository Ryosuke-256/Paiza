import numpy as np
input_line = input()
row_num = int(input_line.split()[1])
col_num = int(input_line.split()[0])
maze = np.empty((row_num,col_num),dtype=int)
for i in range(row_num):
    row = input()
    char_list = row.split()
    convertd_list = [-1 if char == 's' else 2 if char =='g' else int(char) for char in char_list]
    maze[i] = convertd_list
print(maze)
while True

def session(mazelist):
    newmazelist = np.array([])
    for onemaze in mazelist:
        newmaze = function1(onemaze)
        newmazelist = np.concatanate([newmazelist,newmaze])
    return newmazelist


def function1(maze):
    mazelist = np.array([])
    nowpoint = np.where(maze == -1)
    row = nowpoint[0]
    col = nowpoint[1]
    
    if row-1 >=0:
        if maze[row-1,col] == 0:
            newmaze = maze.copy()
            newmaze[row,col] = 1
            newmaze[row-1,col] = -1
            mazelist = np.append(newmaze)
    elif row+1 >=0:
        if maze[row+1,col] == 0:
            newmaze = maze.copy()
            newmaze[row,col] = 1
            newmaze[row+1,col] = -1
            mazelist = np.append(newmaze)
    elif col-1 >=0:
        if maze[row,col-1] == 0:
            newmaze = maze.copy()
            newmaze[row,col] = 1
            newmaze[row,col-1] = -1
            mazelist = np.append(newmaze)
    elif col+1 >=0:
        if maze[row,col+1] == 0:
            newmaze = maze.copy()
            newmaze[row,col] = 1
            newmaze[row,col+1] = -1
            mazelist = np.append(newmaze)
    return mazelist
    
