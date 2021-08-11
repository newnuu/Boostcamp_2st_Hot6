from collections import deque
testcase_num = int(input())
testcase = []

for _ in range(testcase_num):
    temp_lt = []
    for _ in range(3):
        temp_lt.append(list(map(int, input().split())))
    testcase.append(temp_lt)
    
def BFS(l, srt, end):
    visit = [[0] * l for _ in range(l)]
    queue = deque()
    srt_x, srt_y = srt
    end_x, end_y = end
    cnt = 0
    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    visit[srt_x][srt_y] = 1
    queue.append((srt_x, srt_y, cnt))


    while queue:
        a, b, cnt = queue.popleft()

        if a == end_x and b == end_y:
            return cnt
        
        for i in range(8):
            nx, ny = a + dx[i], b + dy[i]
        
            if 0 <= nx <l and 0 <= ny <l and not visit[nx][ny]:
                visit[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))



for i in range(testcase_num):
    print(BFS(testcase[i][0][0], testcase[i][1], testcase[i][2]))


