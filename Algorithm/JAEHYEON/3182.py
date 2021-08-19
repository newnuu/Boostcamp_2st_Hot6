#탐색
def dfs(graph, visited, s, cnt):
    visited[s] = 1
    cnt += 1
    #다음 방문할 곳이 0이 아니고 방문하지 않았다면 탐색하고 cnt 증가
    if graph[graph[s]] != 0 and visited[graph[s]] != 1:
        cnt = dfs(graph, visited, graph[s], cnt)
    return cnt

#방문 초기화
def init_visited(visited):
    for i in range(1, len(visited)):
        visited[i] = 0

N = int(input())

graph = [0 for i in range(N+1)] # 선배들 대답 list
visited = [0 for i in range(N+1)] # 방문확인

for i in range(1, N+1):
    graph[i] = int(input())

max_cnt = 0 # 선배들을 만난 횟수의 최대값
index = N + 1 # 최대값의 index

for i in range(1, N+1):
    cnt = 0
    visited[i] = 1
    # dfs로 각 i마다 선배들을 몇번만나는지 탐색
    cnt = dfs(graph, visited, graph[i] , cnt)
    if cnt > max_cnt:
        max_cnt = cnt
        index = i
    elif cnt == max_cnt:
        if index > i:
            index = i
    init_visited(visited)

print(index)
