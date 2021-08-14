import sys
input = sys.stdin.readline
from collections import deque

def solution(l, f, t):
    move = [(2, 1), (1, 2), (-2, 1), (-1, 2), # 나이트 이동 가중치
            (-2, -1), (-1, -2), (1, -2), (2, -1)]
    visited = [[0]*l for _ in range(l)] # 방문 여부
    Q = deque([(f, 0)])
    visited[f[0]][f[1]] = 1

    while Q: # BFS
        cur, cnt = Q.popleft()
        if cur == t: return cnt # 목적지 도착

        for m in move: # 나이트 이동 경우의 수
            n_loc = (cur[0] + m[0], cur[1] + m[1])
            if (0 <= n_loc[0] < l) and (0 <= n_loc[1] < l): # 체스판 범위 확인
                if visited[n_loc[0]][n_loc[1]] == 0: # 방문 여부 확인
                    visited[n_loc[0]][n_loc[1]] = 1 # 방문
                    Q.append((n_loc, cnt + 1)) # Queue 추가

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        l = int(input())
        f = tuple(map(int, input().split()))
        t = tuple(map(int, input().split()))
        result = solution(l, f, t)
        print(result)
