from collections import deque
from sys import stdin
import sys
sys.setrecursionlimit(20000)
input = stdin.readline

def dfs(graph, visited, x, y, N):
    # 이동 가중치
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = 1 # 방문
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 넘어간다면
        if (nx < 0 or nx >= N or ny < 0 or ny >= N):
            continue
        # graph[x][y] == graph[nx][ny] 이고 아직 방문하지 않았다면
        elif (graph[x][y] == graph[nx][ny] and visited[nx][ny] == 0):
            dfs(graph, visited, nx, ny, N) # 재귀호출

if __name__ == "__main__":
    N = int(input())
    graph = [list(input()) for _ in range(N)] # R,G,B 값을 저장하는 2차원 배열
    visited = [[0] * N for _ in range(N)] # 방문했는지 체크하는 2차원 배열
    cnt_1 = 0 # 색약x count
    cnt_2 = 0 # 색약o count

    #색약이 아닐경우
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                cnt_1 += 1
                dfs(graph, visited, i, j, N)

    # 색약일 경우를 위해 R을 모두 G로 바꿈
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'R':
                graph[i][j] = 'G'
    
    visited = [[0] * N for _ in range(N)] # 방문 2차원 배열 초기화

    #색약일 경우
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                cnt_2 += 1
                dfs(graph, visited, i, j, N)
    
    print(cnt_1, cnt_2)
