import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

def solution(N, fig):
    D = [(1,0), (0,1), (-1,0), (0,-1)] # 이동 가중치
    visited_1 = [[0] * N for _ in range(N)] # 적록색약X 방문
    visited_2 = [[0] * N for _ in range(N)] # 적록색약  방문

    def dfs(loc, c, visited): # (xy, colors, 적록색약 여부에 따른 방문 배열)
        visited[loc[0]][loc[1]] = 1 # 방문표시
        for d in D: # 동서남북 탐색
            nr, nc = (loc[0] + d[0], loc[1] + d[1])
            if (0 <= nr < N) and (0 <= nc < N):
                if visited[nr][nc] == 0 and fig[nr][nc] in c: # 방문 x and 같은 색
                    dfs((nr, nc), c, visited)

    answer = [0, 0]
    for row in range(N): # dfs 시작 좌표
        for col in range(N):
            color = [fig[row][col]]
            if visited_1[row][col] == 0: # 적록색약X
                dfs((row, col), color, visited_1)
                answer[0] += 1
            if visited_2[row][col] == 0: # 적록색약
                if color[0] in ['R', 'G']: color = ['R', 'G']
                dfs((row, col), color, visited_2)
                answer[1] += 1

    return str(answer[0]) + ' ' + str(answer[1])

if __name__ == '__main__':
    N = int(input())
    fig = [input().strip() for _ in range(N)]
    result = solution(N, fig)
    print(result)
