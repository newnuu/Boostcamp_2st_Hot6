import sys
from collections import deque
input = sys.stdin.readline

# 말처럼 이동 가중치
h_dx = [-1, -2, -2, -1, 1, 2, 2, 1]
h_dy = [-2, -1, 1, 2, 2, 1, -1, -2]

# 원숭이처럼 이동 가중치
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

K = int(input()) # 말처럼 이동할 수 있는 횟수
W , H = map(int, input().split()) # 가로길이 W, 세로길이 H
graph = [list(map(int, input().split())) for i in range(H)]

def bfs():
    queue = deque()
    queue.append((0, 0, K))

    # 방문체크 3중 배열
    # 말처럼 이동한 경우 / 원숭이처럼 이동한 경우 구별
    visited = [[[0] * (K + 1) for i in range(W)] for i in range(H)]
    while queue:
        x, y, k = queue.popleft()

        # 도착지점에 도달했다면
        if x == H - 1 and y == W - 1:
            return visited[x][y][k]

        # 원숭이처럼 이동한 경우 (K 변화 X)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= H or ny >= W:
                continue
            # 장애물이 없고 아직 방문하지 않았다면
            if graph[nx][ny] != 1 and visited[nx][ny][k] == 0:
                visited[nx][ny][k] = visited[x][y][k] + 1
                queue.append((nx, ny, k))

        # 말처럼 이동한 경우 (K 변화 O)
        if k > 0:
            for i in range(8):
                nx = x + h_dx[i]
                ny = y + h_dy[i]
                if nx < 0 or ny < 0 or nx >= H or ny >= W:
                    continue
                # 장애물이 없고 아직 방문하지 않았다면
                if graph[nx][ny] != 1 and visited[nx][ny][k-1] == 0:
                    visited[nx][ny][k-1] = visited[x][y][k] + 1
                    queue.append((nx, ny, k-1)) # k 하나 빼줌

    return -1

print(bfs())
