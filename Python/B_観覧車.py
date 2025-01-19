import numpy as np
input_line = input()
gondra = int(input_line.split()[0])
group = int(input_line.split()[1])
gondra_limit = np.zeros(gondra,dtype=int)
for i in range(gondra):
    row = int(input())
    gondra_limit[i] = row
gondra_count = np.zeros(gondra,dtype=int)
gondra_seq = 0

for i in range(group):
    menber_num = int(input())
    threthold = 0
    while threthold < menber_num:
        nowgondra = gondra_seq%gondra
        if threthold+gondra_limit[nowgondra] >= menber_num:
            break
        threthold += gondra_limit[nowgondra]
        gondra_count[nowgondra] += gondra_limit[nowgondra]
        gondra_seq += 1
    nowgondra = gondra_seq%gondra
    gondra_count[nowgondra] += (menber_num - threthold)
    gondra_seq += 1

for i in range(gondra):
    print(int(gondra_count[i]))