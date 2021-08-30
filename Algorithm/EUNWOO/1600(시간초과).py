import heapq
import copy
import sys
input = sys.stdin.readline
k = int(input())
w,h = map(int,input().split())
board = []
visited=[[0 for _ in range(w)] for _ in range(h)]

for _ in range(h):
    board.append(list(map(int,input().split())))

horse = [(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1)] # 말이 움직일 수 있는 자리
m = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우

q=[]
heapq.heapify(q)
heapq.heappush(q,(0,0,0,0,visited))
visited[0][0]=1

while q:
    x,y,cnt,mcnt,visited = heapq.heappop(q) # 좌표값이 큰 곳 부터 
    if cnt<k: # 말처럼 움직이는횟수 남은 경우
        for dx,dy in horse:
            xx,yy = -x+dx,-y+dy
            if xx== h-1 and yy==w-1: # 도착
                print(cnt+mcnt+1)
                exit()
            if xx<w and xx>=0 and yy<h and yy>=0 and not visited[xx][yy] and not board[xx][yy]:
                v = copy.deepcopy(visited) # 각 시점에서의 visited
                v[xx][yy]=1
                heapq.heappush(q,(-xx,-yy,cnt+1,mcnt,v))

    for dx,dy in m: # 상하좌우로 먼저 움직여야 할 경우도 있어서 모든 경우 계산
        xx,yy = -x+dx,-y+dy
        if xx== h-1 and yy==w-1:
            print(cnt+mcnt+1)
            exit()
        if xx<w and xx>=0 and yy<h and yy>=0 and not visited[xx][yy] and not board[xx][yy]:
            v = copy.deepcopy(visited)
            v[xx][yy]=1
            heapq.heappush(q,(-xx,-yy,cnt,mcnt+1,v))
print(0)
