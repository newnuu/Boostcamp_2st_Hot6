from sys import stdin
from collections import deque
input = stdin.readline


# 영상변환 리스트 생성.
def _21938(N : int, M : int, image : list, T : int):

    display = [[] for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    
    for idx, val in enumerate(image):
        for j in range(0, 3 * M, 3):
            a = sum(val[j : j + 3]) / 3
            display[idx].append(255 if a >= T else 0)
            
    return BFS(display, visit)


# BFS로 물체 갯수 탐색.
def BFS(graph : list, visit : list):

    ans = 0
    queue = deque()
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            if not visit[i][j] and graph[i][j] == 255:
                visit[i][j] = 1
                queue.append([i, j])
                ans += 1    

                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]

                        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and graph[nx][ny] == 255:
                            visit[nx][ny] = 1
                            queue.append([nx, ny])
    
    return ans



if __name__ == "__main__":
    N, M = map(int, input().split())
    image = [list(map(int, input().split())) for _ in range(N)]
    T = int(input())

    print(_21938(N, M, image, T))
