# 10026번 적록색약  골드 5

from collections import deque

n = int(input())
data = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  
  while queue:
    x, y = queue.popleft()
        
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n:
        if data[nx][ny] == data[x][y] and visited[nx][ny] == 0:
          queue.append((nx, ny))
          visited[nx][ny] = 1

cnt = 0
for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      bfs(i, j)
      cnt += 1
print(cnt, end=' ')

for i in range(n):
  for j in range(n):
    if data[i][j] == 'R':
      data[i][j] = 'G'
visited = [[0] * n for _ in range(n)]

cnt = 0
for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      bfs(i, j)
      cnt += 1
print(cnt)
