import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

def solution(N, M, K, X, loads):
    graph = defaultdict(list)
    fee = [float('inf')] * (N+1)
    fee[X] = 0 # 시작점 cost

    for f, t in loads: # graph 초기화
        graph[f].append(t)

    Q = [(fee[X], X)]

    while Q: # 다익스트라
        cur_fee, cur_n = heapq.heappop(Q)
        if cur_fee > K: break # 탐색 종료
        if fee[cur_n] < cur_fee: continue

        for next_n in graph[cur_n]: # 이어진 노드 탐색
            if cur_fee + 1 < fee[next_n]:
                fee[next_n] = cur_fee + 1
                heapq.heappush(Q, (cur_fee + 1, next_n))

    answer = [str(i) for i in range(N+1) if fee[i] == K]

    return '\n'.join(answer) if len(answer) > 0 else -1

if __name__ == '__main__':
    N, M, K, X = map(int, input().split())
    loads = [tuple(map(int, input().split())) for i in range(M)]
    result = solution(N, M, K, X, loads)
    print(result)
