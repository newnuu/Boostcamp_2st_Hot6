from sys import stdin
import heapq

input = stdin.readline

def _18352(N, M, K, X):
    INF = 300001
    city = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    for _ in range(M):
        srt, end = map(int, input().split())
        city[srt].append((end, 1))
    
    q = []
    heapq.heappush(q, (0, X))
    distance[X] = 0

    while q:
       dist, loc = heapq.heappop(q)
       if distance[loc] < dist: continue
       for i in city[loc]:
           cost = dist + i[1]
           if cost < distance[i[0]]:
               distance[i[0]] = cost
               heapq.heappush(q, (cost, i[0]))

    answer = []
    for i in range(1, N + 1):
        if distance[i] == K:
            answer.append(i)
    
    if len(answer) == 0:
        print(-1)
    else:
        for i in answer:
            print(i)


if __name__ == "__main__":
    N, M, K, X = map(int, input().split())
    _18352(N, M, K, X)
        
