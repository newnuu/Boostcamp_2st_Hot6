from collections import deque

com = int(input())
pair = int(input())

graph = [[0] * (com + 1) for _ in range(com + 1)] # graph 2차원 배열
visited = [0 for _ in range(com + 1)] #방문했는지 check 하는 배열

for _ in range(pair):
    # 방향이 없는 그래프 이므로 (x, y) (y, x) 모두 1로 바꿔줘야함
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def bfs (start):
    cnt = 0 # 몇대까지 걸렸는지 count 하는 변수
    queue = deque()
    queue.append(start)
    visited[start] = 1 
    while queue:
        x = queue.popleft()

        for y in range(len(graph[start])):
            # graph[x][y]가 1이고 아직 방문하지 않았다면
            if graph[x][y] == 1 and visited[y] == 0:
                visited[y] = 1 # 해당 노드를 1로 바꾸고
                queue.append(y) # queue에 추가
                cnt += 1 # cnt 1 증가
    return cnt


print(bfs(1))
