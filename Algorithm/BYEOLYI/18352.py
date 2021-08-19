# 18352번 | 특정 거리의 도시 찾기 | 실버 2

from collections import deque

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
  a, b = map(int, input().split())
  # graph[1] == [2, 3], graph[2] == [3, 4]
  graph[a].append(b)

# 모든 도시에 대해 k로부터 최단 거리
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
  now = q.popleft()
  # 현재 도시에서 이동할 수 있는 모든 도시를 확인
  for next_node in graph[now]:
    # 아직 방문하지 않은 도시라면
    if distance[next_node] == -1:
      # 최단 거리 갱신
      distance[next_node] = distance[now] + 1
      q.append(next_node)
  
# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1) :
  if distance[i] == k:
    print(i)
    check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
  print(-1)
