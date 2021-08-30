'''
https://www.acmicpc.net/problem/1600
말이 되고픈 원숭이
[풀이]
1. 일반적인 bfs 문제와 동일
2. 다만, K에 따라 방문처리를 다르게 해야해서 방문 리스트를 3차원으로 선언한다.
'''
from collections import deque
import sys
input = sys.stdin.readline
K = int(input())
M, N = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
horse_move = [(i, j) for i in [-2, -1, 1, 2] for j in [3-abs(i), abs(i)-3]]

def bfs():
    visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
    q = deque([(0, 0, K)])

    while q:
        y, x, k = q.popleft()
        cost = visited[y][x][k]
        if y == N - 1 and x == M - 1:
            return cost

        for dy, dx in move:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and not board[ny][nx] and not visited[ny][nx][k]:
                visited[ny][nx][k] = cost + 1
                q.append((ny, nx, k))

        if not k:
            continue

        for dy, dx in horse_move:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and not board[ny][nx] and not visited[ny][nx][k-1]:
                visited[ny][nx][k-1] = cost + 1
                q.append((ny, nx, k-1))

    return -1

print(bfs())
