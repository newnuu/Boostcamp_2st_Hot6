import sys
from collections import deque
input = sys.stdin.readline

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)] # 연결 정보 담은 list
answer = [-1] * (N + 1) # 거리 정보 담을 list
answer[X] = 0 # 출발 도시 0

# 연결 정보 입력
for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

queue = deque([X]) # 시작점 입력

#BFS
while queue:
    now = queue.popleft()
    for next in graph[now]:
        # now에 연결된 도시에 아직 방문하지 않았다면
        if answer[next] == -1:
            answer[next] = answer[now] + 1 # 현재 도시 + 1
            queue.append(next)

for i in range(N + 1):
    if answer[i] == K:
        print(i)

# 최단 거리가 K인 도시가 존재 x
if K not in answer:
    print(-1)
