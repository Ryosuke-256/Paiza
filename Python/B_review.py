N,M,K = map(int, input().split())
row = input()
mine = [int(char) for char in row.split()]
recomend = set()
for _ in range(M):
    other = list(map(int, input().split())) 
    same_count = sum(1 for j in range(N) if mine[j] == other[j] == 3)
    if same_count < K:  
        continue
    for j in range(N):
        if mine[j] == 0 and other[j] == 3:
            recomend.add(j + 1) 
if not recomend:
    print('no')
else:
    print(" ".join(map(str, sorted(recomend))))  