'''
https://www.acmicpc.net/problem/21938
영상처리
[풀이]
1. 각 행마다 split 해서 int형으로 입력받는다
2. 3칸씩 원소의 합을 구해 경계값의 3배보다 큰지 작은지 조사한다
3. 이후 bfs로 물체의 개수를 구한다
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
thr = int(input()) * 3
board = [[sum(b[3*idx:3*(idx+1)])>=thr for idx in range(len(b)//3)] for b in board]

for y in range(N):
    for x in range(M):
        if board[y][x]:
            stack = set([(y, x)])
            board[y][x] = 2
            while stack:
                _y, _x = stack.pop()
                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ny, nx = _y+dy, _x+dx
                    if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1:
                        board[ny][nx] = False
                        stack.add((ny, nx))

print(sum([b.count(2) for b in board]))
