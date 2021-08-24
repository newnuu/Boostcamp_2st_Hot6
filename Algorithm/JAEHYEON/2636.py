import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0] # x 가중치
dy = [0, 1, 0, -1] # y 가중치

h, w = map(int, input().split(' ')) # height, width
graph = []

for _ in range(h):
    graph.append(list(map(int, input().split(' ')))) # 그래프 입력

count = 0 # 치즈의 갯수 count
for i in range(h):
    for j in range(w):
        if graph[i][j] == 1:
            count += 1

# 공기와 접촉하고 있는 치즈들에 대한 탐색
def bfs(count):
    while queue:
        xy = queue.popleft()

        for i in range(4):
            x = xy[0]
            y = xy[1]
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0 or ny < 0 or nx >= h or ny >= w):
                continue
            elif visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if graph[nx][ny] == 1:
                    # 공기와 접촉한 치즈들은 값을 2로 전환
                    graph[nx][ny] = 2
                    # 치즈 갯수 감소
                    count -= 1
                else:
                    queue.append([nx, ny])
    return count

# 공기중과 접촉한 치즈 삭제
def delete():
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 2:
                graph[i][j] = 0

queue = deque()

hour = 0 # 걸린 시간
remain_count = count # 남은 치즈 갯수

# 남은 치즈가 0이 될때까지 반복
while count != 0:
    visited = [[0 for _ in range(w)] for _ in range(h)]
    queue.append([0, 0])
    visited[0][0] = 1
    count = bfs(count)
    if count != 0:
        remain_count = count

    hour += 1
    delete()

print(hour)
print(remain_count) 
