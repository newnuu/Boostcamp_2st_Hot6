n,m = map(int,input().split())
sq = []
mi = min(n,m)
for i in range(n):
    sq.append(str(input()))
while True:
    for i in range(n):
        if i+mi<=n:
            for j in range(m-mi+1):
                if sq[i][j]!=sq[i][j+mi-1]:
                    continue
                else:
                    if sq[i+mi-1][j]!=sq[i][j] or sq[i][j]!=sq[i+mi-1][j+mi-1]:
                        continue
                    else:
                        print(mi**2)
                        exit(0)
    mi-=1
