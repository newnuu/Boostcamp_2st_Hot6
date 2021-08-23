from sys import stdin
from collections import deque
input = stdin.readline

# 구멍이라면 탐색했을 때 치즈틀에 도달 할 수 없음 <- 이걸 생각 못하고 치즈 가장자리만 구분해 내려고 개고생

def _2636(R : int, C : int, borad : list):
    visited = [[0] * C for _ in range(R)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if not board[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                else:
                    board[nx][ny] = 0
                    cnt += 1
                    visited[nx][ny] = 1 
    ans.append(cnt)
    return cnt


if __name__ == '__main__':
    R, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    ans = []
    t = 0

    while True:
        t += 1
        cnt = _2636(R, C, board)
        if cnt == 0:
            break

    print(t - 1)
    print(ans[-2])
