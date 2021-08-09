import sys
input = sys.stdin.readline
from collections import deque

def solution(l, f, t):
    move = [(2, 1), (1, 2), (-2, 1), (-1, 2),
            (-2, -1), (-1, -2), (1, -2), (2, -1)]
    visited = [[0]*l for _ in range(l)]
    Q = deque([(f, 0)])
    visited[f[0]][f[1]] = 1

    while Q:
        cur, cnt = Q.popleft()
        if cur == t: return cnt

        for m in move:
            n_loc = (cur[0] + m[0], cur[1] + m[1])
            if (0 <= n_loc[0] < l) and (0 <= n_loc[1] < l):
                if visited[n_loc[0]][n_loc[1]] == 0:
                    visited[n_loc[0]][n_loc[1]] = 1
                    Q.append((n_loc, cnt + 1))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        l = int(input())
        f = tuple(map(int, input().split()))
        t = tuple(map(int, input().split()))
        result = solution(l, f, t)
        print(result)
