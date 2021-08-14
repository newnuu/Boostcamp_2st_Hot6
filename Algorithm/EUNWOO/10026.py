import sys
sys.setrecursionlimit(20000)

def dfs(x,y,c,g,vs): # 같은 색 탐색 - 좌표 x,y , 색깔 c, grid g, visited 확인 vs
    if g[x][y]!=c:
        vs[x][y]=0
        return
    for dx,dy in move:
        xx,yy = x+dx,y+dy
        if xx<0 or yy<0 or yy>=n or xx>=n:
            continue
        if not vs[xx][yy]:
            vs[xx][yy]=1
            dfs(xx,yy,c,g,vs)
    
n = int(input())
grid = []
grid2=[[] for _ in range(n)]

for i in range(n):
    grid.append(list(input()))
    grid2[i] = grid[i][:]
    
color = ['R','G','B']

answer=[0,0,0]
answer2=[0,0,0]

move = [(1,0),(0,-1),(-1,0),(0,1)] # 이동 방향

visited = [[0 for _ in range(n)] for _ in range(n)]
visited2 = [[0 for _ in range(n)] for _ in range(n)]

# 'G' 를 'R'로 바꿔주기 (적록색약)
for i in range(n):
    for j in range(n):
        if grid2[i][j]=="G":
            grid2[i][j]="R"   
            
for i in range(n):
    for j in range(n):  
      
        # 일반 사람
        if visited[i][j]==0: # 방문 안한 점에 대해서 같은 색 탐색
            dfs(i,j,grid[i][j],grid,visited) # 같은 색을 모두 돌고 나오면 dfs 종료
            answer[color.index(grid[i][j])]+=1 # 1 구역 추가
        
        # 적록색약    
        if visited2[i][j]==0:
            dfs(i,j,grid2[i][j],grid2,visited2)
            answer2[color.index(grid2[i][j])]+=1
                    
print(sum(answer),sum(answer2))
            
    

    
