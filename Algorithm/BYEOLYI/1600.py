# 1600번 | 말이 되고픈 원숭이 | 골드 4

from collections import deque

# BFS 소스코드 구현
def bfs():
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque()
  queue.append((0, 0, k))
  visited = [[[0 for _ in range(31)] for _ in range(w)] for _ in range(h)]

  # 큐가 빌 때까지 반복
  while queue:
    x, y, z = queue.popleft()

    if x == h - 1 and y == w - 1:
      return visited[x][y][z]
    
    if z > 0:
      for i in range(8):
        nx = x + dxk[i]
        ny = y + dyk[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1 and visited[nx][ny][z - 1] == 0:
          visited[nx][ny][z - 1] = visited[x][y][z] + 1
          queue.append((nx, ny, z - 1))
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1 and visited[nx][ny][z] == 0:
        visited[nx][ny][z] = visited[x][y][z] + 1
        queue.append((nx, ny, z))
        
  return -1

k = int(input())
# 격자판의 가로길이 W, 세로길이 H
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

# k번 이동할 수 있는 방향 정의
dxk = [1, 2, 2, 1, -1, -2, -2, -1]
dyk = [2, 1, -1, -2, -2, -1, 1, 2]
    
# k번 이외 이동할 수 있는 방향 정의
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

print(bfs())
