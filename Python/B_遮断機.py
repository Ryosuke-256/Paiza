import numpy as np
input_line = input()
train = int(input_line.split()[0])
interval = int(input_line.split()[1])
table = np.zeros(train,dtype=int)
syadan = np.zeros(train,dtype=int)

comingtime = int(input())
table[0] = comingtime
if table[0] > interval:
    syadan[0] = interval
else:
    syadan[0] = table[0]
    
for i in range(1,train):
    comingtime = int(input())
    table[i] = comingtime
    if table[i]-table[i-1] > interval:
        syadan[i] = interval
    else:
        syadan[i] = syadan[i-1] + table[i]-table[i-1]

print(max(syadan))