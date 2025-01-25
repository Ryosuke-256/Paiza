
import numpy as np
row_num,col_num = map(int, input().split())
table = np.zeros((row_num,col_num),dtype=int)
for i in range(row_num):
    oneline = input()
    table[i] = list(map(int,oneline.split()))
    
path_scores = []

def dfs_stack(table,position):
    stack = [(position,0,[])]
    
    while stack:
        node,current_score,visited_path = stack.pop()
        row,col = node
        visited_path = visited_path + [node]
        current_score += table[row,col]
        
        if row == row_num - 1:
            path_scores.append((visited_path,current_score))
        else:
            next_pos = []
            if col > 0:
                next_pos.append((row + 1, col - 1))
            if col < col_num - 1:
                next_pos.append((row + 1, col + 1))
            next_pos.append((row + 1,col))
            
            for pos in next_pos:
                stack.append((pos,current_score,visited_path))

for i in range(col_num):
    dfs_stack(table,(0,i))
max_score_path = max(path_scores, key=lambda x: x[1])
print(max_score_path[1])