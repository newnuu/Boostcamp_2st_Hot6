import sys
sys.setrecursionlimit(10**6)

n,m  = map(int,input().split())
display = []
px = []

for i in range(n):
    display.append(list(map(int,input().split())))
    px.append([])
    for j in range(m):# 평균값 계산
        px[-1].append(sum(display[-1][3*j:3*j+3])//3)
        
t = int(input())

# 경계값보다 크면 물체 인식
for i in range(n):
    for j in range(m):
        if px[i][j]<t:
            px[i][j] = 0
        else:
            px[i][j]=255

move = [(-1,0),(1,0),(0,1),(0,-1)]
visited=[[0 for _ in range(m)] for _ in range(n)]
# 인접해 있는 물체 하나로 인식하기
def dfs(x,y):
    for dx,dy in move:
        xx,yy = x+dx,y+dy
        if xx<n and xx>=0 and yy<m and yy>=0:
            if not visited[xx][yy] and px[xx][yy]==255:
                visited[xx][yy]=1
                dfs(xx,yy)
answer=0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and px[i][j]==255: # 방문하지 않았고, 물체가 있는 자리면 dfs
            dfs(i,j)
            answer+=1
print(answer)
