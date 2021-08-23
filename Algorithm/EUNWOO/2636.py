import collections
import sys
input = sys.stdin.readline

def bfs(x,y):
    q=collections.deque()
    q.append((x,y))
    tmp=[]
    
    while q:
        x,y = q.popleft()
        cheese[x][y]=-1 # 외부
        for dx,dy in move:
            xx,yy = x+dx,y+dy
            if xx<r and xx>=0 and yy<c and yy>=0:
                if cheese[xx][yy]==0: # 외부 설정
                    cheese[xx][yy]=-1
                    q.append((xx,yy))
                if cheese[xx][yy]==1 and cheese[x][y]==-1: # 외부와 닿아있는 치즈
                    tmp.append((xx,yy))
    return tmp

r,c = map(int,input().split())
cheese = []
move = [(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(r):
    cheese.append(list(map(int,input().split())))
    
cnt = 1
ch = collections.deque(set(bfs(0,0))) # 외부와 닿아있는 치즈 부분

while True:
    tmp = []
    last = len(ch)
    while ch:
        for side in ch:
            x,y = side[0],side[1]
            cheese[x][y] = 0
        x,y = ch.popleft()
        tmp+=bfs(x,y)
    if tmp ==[]: # 치즈 부분 모두 없어지면 
        break
    else:
        ch = collections.deque(set(tmp))
        cnt+=1
        
print(cnt,last,sep='\n')
