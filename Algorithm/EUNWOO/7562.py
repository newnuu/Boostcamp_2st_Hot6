import collections

def bfs(s1,s2,d1,d2):
    q = collections.deque()
    q.append((0,s1,s2))
    visited[s1][s2]=1
    
    while q:
        cnt, x,y = q.popleft()
        if x==d1 and y==d2:
            print(cnt)
            return
          
        for dx,dy in move:
            if x+dx>=l or x+dx<0 or y+dy>=l or y+dy<0: # 범위 벗어나면 continue
                continue
            if not visited[x+dx][y+dy]: # 이전에 방문하지 않았으면 q에 넣기
                visited[x+dx][y+dy]=1
                q.append((cnt+1,x+dx,y+dy)) 
            
                
t = int(input())
move = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)] # 움직일 수 있는 방향

for _ in range(t):
    l = int(input())
    s1,s2 = map(int, input().split()) # 출발지
    d1,d2 = map(int,input().split()) # 도착지
    visited = [[0 for _ in range(l)] for _ in range(l)]
    bfs(s1,s2,d1,d2)
