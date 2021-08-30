import collections

n,m = map(int,input().split())
f = [[0,0,0,0]] # 흥미도
l = [] # 연꽃

for _ in range(n):
    f.append(list(map(int,input().split())))
for _ in range(n):
    l.append(list(set(map(int,input().split()))))

# 연결된 통나무 양쪽의 흥미도 확인 
for _ in range(m):
    a,b,t = map(int,input().split())
    if f[a][t-1]!=f[b][t-1]:
        print("NO")
        exit()

# 선호하는 연꽃 배치
loc = [0 for _ in range(n+1)]
loc[0]=-1
while 0 in loc:
    for i in range(n):
        if len(l[i])==1: # 가능한 연꽃이 하나이면 그 자리 배치
            loc[l[i][0]]=i+1
            for j in range(n): # 정해진 자리는 다른 개구리들의 선호 연꽃에서 삭제
                if j !=i and l[i][0] in l[j]:
                    l[j].remove(l[i][0])
                    
    if 0 not in loc and max([len(ll) for ll in l])==1: # 모든 자리에 배치가 되었거나 선호하는 자리가 1개씩이 되면 break
        break
    if min([len(ll) for ll in l])==0: # 자리배치 불가능한 경우 
        print("NO")
        exit()
        
print(*loc[1:])
