# 2606번 바이러스 실버 3

from collections import deque

computers = int(input()) # 컴퓨터의 수
connection = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
data = [[0] * (computers + 1) for _ in range(computers + 1)]
visited = [0 for _ in range(computers + 1)]

def bfs():
  result = 0 # 1번 컴퓨터 제외
  queue = deque()
  queue.append(1)
  visited[1] = 1 # 1번 컴퓨터에 바이러스

  while queue:
    a = queue.popleft()

    # 0번은 사용하지 않음
    for i in range(1, computers + 1):
      if data[a][i] == 1 and visited[i] == 0:
        visited[i] = 1
        result += 1
        queue.append(i)
  
  return result

for _ in range(connection):
  x, y = map(int, input().split())
  data[x][y] = 1
  data[y][x] = 1
      
print(bfs())
