r,c = map(int,input().split())
board = []
for _ in range(r):
    board.append(input())
    
move = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(x,y):
    global result
    q = set()
    q.add((x,y,board[x][y]))
    
    while q:
        x,y,step = q.pop()
        result = max(result,len(step)) # 항상 가장 긴 값 저장
        for dx,dy in move:
            xx,yy = x+dx,y+dy
            if xx<r and xx>=0 and yy<c and yy>=0 and board[xx][yy] not in step:
                q.add((xx,yy,step+board[xx][yy]))
                
result=0  
bfs(0,0)
print(result)
