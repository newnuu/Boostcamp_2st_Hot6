import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0] # x 가중치
dy = [0, -1, 0, 1] # y 가중치

def bfs(s_x , s_y, R, C, graph, answer):
    # start x, start y, graph값 queue에 입력
    queue = set([(s_x, s_y, graph[s_x][s_y])])
    while queue:
        x, y, ans = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            # 만약 ans 안에 중복되는 알파벳이 없다면
            elif graph[nx][ny] not in ans:
                queue.add((nx, ny, ans + graph[nx][ny])) #추가
                answer = max(answer, len(ans) + 1) # answer 업데이트
    return answer
        

R, C = map(int, input().split()) # 세로 R, 가로 C
graph = [list(input().strip()) for _ in range(R)] # 알파벳 그래프
answer = 1
answer = bfs(0, 0, R, C, graph, answer) # 탐색
print(answer)
