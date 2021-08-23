# 2636번 | 치즈 | 골드 5

from collections import deque

def bfs(h, w, graph):
  queue = deque()
  queue.append((0, 0))
  check = [[False] * w for _ in range(h)]
  # 상하좌우
  dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
  count = 0
  
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]

      # 범위를 벗어나지 않는 경우
      if 0 <= nx < h and 0 <= ny < w:

        # 공기와 맞닿은 부분이고 한 번도 방문하지 않은 경우
        if graph[nx][ny] == 0 and check[nx][ny] == False:
          check[nx][ny] = True
          queue.append((nx, ny))
      
        # (0, 0) 에서 시작해서 처음 만나는 1들은 모두 가장자리
        elif graph[nx][ny] == 1:
          # queue에 추가하지 않고 0으로 바꿔 치즈 녹임
          graph[nx][ny] = 0
          count += 1
          check[nx][ny] = True

  return count

# 세로와 가로의 길이
h, w = map(int, input().split())
# 판
graph = [list(map(int, input().split())) for _ in range(h)]
result = []
turn = 0

while True:
  count = bfs(h, w, graph)
  result.append(count)
  # 치즈가 모두 녹은 경우
  if count == 0:
    break
  turn += 1

print(turn)
print(result[-2])
