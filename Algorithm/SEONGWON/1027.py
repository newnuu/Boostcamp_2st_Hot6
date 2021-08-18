import sys
input = sys.stdin.readline

def solution(N, heights):
    counts = [0] * N # 해당 건물에서 볼 수 있는 다른 건물 수
    weight = lambda x1,y1,x2,y2 : (y2 - y1) / (x2 - x1) # 기울기 구하기

    for x in range(N): # 브루트포스
        l_w, r_w = float('inf'), -float('inf') # left는 min 방향 탐색, right는 max 방향 탐색이므로

        for l_x in range(x - 1, -1, -1): # 왼쪽 건물들 탐색
            n_w = weight(x, heights[x], l_x, heights[l_x]) # 기울기
            if n_w < l_w: # 더 작아지면 갱신 및 count ++
                l_w = n_w
                counts[x] += 1

        for r_x in range(x + 1, N):
            n_w = weight(x, heights[x], r_x, heights[r_x])
            if n_w > r_w: # 더 커지면 갱신 및 count ++
                r_w = n_w
                counts[x] += 1

    return max(counts)

if __name__ == '__main__':
    N = int(input())
    heights = list(map(int, input().split()))
    result = solution(N, heights)
    print(result)
