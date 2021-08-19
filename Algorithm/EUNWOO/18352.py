import collections
import sys

n,m,k,x = map(int,sys.stdin.readline().split())
road = collections.defaultdict(list)
for _ in range(m):
    s,d = map(int,sys.stdin.readline().split())
    road[s].append(d)
    
q=collections.deque()
q.append((0,x))

ans=[]
visited = [0 for _ in range(n+1)]
visited[x] = 1 # 시작점

while q:
    dist, ct = q.popleft() 
    
    if dist==k: # 거리 k이면 정답 리스트에 넣기
        ans.append(ct)
        
    for c in road[ct]: # 연결된 도시들 중 방문 안 한 도시 방문
        if not visited[c]:
            visited[c]=1
            q.append((dist+1,c)) # 거리 +1 
            
ans.sort()            
if not ans:
    print(-1)
else:
    for i in ans:
        print(i)
