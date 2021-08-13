from collections import deque
from sys import stdin
input = stdin.readline

def bfs(graph, visited, s_x, s_y, e_x, e_y, I):
    # 나이트 이동 방향
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    queue = deque()
    visited[s_x][s_y] = 1 # 시작지점 방문
    queue.append((s_x, s_y))
    while queue:
        xy = queue.popleft()
        x = xy[0]
        y = xy[1]
        # 해당 지점이 가고자 했던 지점이라면
        if e_x == x and e_y == y: 
            return graph[x][y]
        for i in range(8): 
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 넘어간다면
            if (nx < 0 or ny < 0 or nx >= I or ny >= I): 
                continue
            # graph[nx][ny] 값이 0이고 아직 방문하지 않았다면
            elif(graph[nx][ny] == 0 and visited[nx][ny] == 0): 
                visited[nx][ny] = 1 # 방문
                graph[nx][ny] = graph[x][y] + 1 # 전 지점에서 1증가
                queue.append((nx, ny)) # queue에 추가

        
if __name__ == "__main__":
    T = int(input()) # Testcase
    while T:
        I = int(input()) # 체스판 크기
        graph = [[0] * I for _ in range(I)] # 나이트 이동을 저장할 2차원 배열
        visited = [[0] * I for _ in range(I)] # 방문했는지 체크하는 2차원 배열
        s_x, s_y = map(int, input().split()) # 시작점
        e_x, e_y = map(int, input().split()) # 가고자하는 목표점
        print(bfs(graph, visited, s_x, s_y, e_x, e_y, I))
        T += -1
