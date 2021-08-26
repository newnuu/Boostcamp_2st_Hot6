import sys
from collections import deque
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 같은 물체 찾기 bfs
def bfs(x, y, T, visited, sum_arr):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 탐색했을때 임계값을 넘는 곳이고 인접한데 방문하지 않았다면
            if visited[nx][ny] == 0 and sum_arr[nx][ny] >= T:
                visited[nx][ny] = 1
                queue.append((nx, ny))


N, M = map(int, input().split()) # 가로 N, 세로 M

sum_arr = [] # 픽셀의 평균값을 담을 리스트
for _ in range(N):
    input_list = list(map(int, input().split()))
    temp = []
    for k in range(M):
        # 3개씩 더하고 평균내기
        temp.append(int(sum(input_list[3*k:3*(k+1)]) / 3))
    sum_arr.append(temp)

T = int(input()) # 경계값

visited = [[0 for _ in range(M)] for _ in range(N)] # 방문 check

cnt = 0 # 물체

# 같은 물체 찾기
for x in range(N):
    for y in range(M):
        if sum_arr[x][y] >= T and visited[x][y] == 0:
            bfs(x, y, T, visited, sum_arr)
            cnt += 1

print(cnt)
