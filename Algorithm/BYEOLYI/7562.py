# 7562번  나이트의 이동  실버 3
# 소요 시간 : 51분 20초

from collections import deque

t = int(input()) # 테스트 케이스의 개수

# 이동할 8 방향 정의
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

# BFS 소스코드 구현
def bfs():
  l = int(input()) # 체스판의 한 변의 길이
  chess = [[0] * l for _ in range(l)] # 체스판의 크기는 l × l
  now_x, now_y = map(int, input().split()) # 나이트가 현재 있는 칸
  move_x, move_y = map(int, input().split()) # 나이트가 이동하려고 하는 칸
  result = 0 # 결과 값
  
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque()
  queue.append((now_x, now_y))

  # 큐가 빌 때까지 반복
  while queue:
    now_x, now_y = queue.popleft()

    # 현재 위치와 이동하려는 위치가 같은 경우
    if now_x == move_x and now_y == move_y:
      break

    # 현재 위치에서 8 방향으로의 위치 확인
    for i in range(8):
      nx = now_x + dx[i]
      ny = now_y + dy[i]
    
      # 체스판을 벗어난 경우 무시
      if nx < 0 or ny < 0 or nx >= l or ny >= l:
        continue
      
      if chess[nx][ny] == 0:
        chess[nx][ny] = chess[now_x][now_y] + 1
        queue.append((nx, ny))

  # 최단거리 return
  return chess[move_x][move_y]
    
for _ in range(t):
  print(bfs())
