from sys import stdin
input = stdin.readline

def _1027(n : int, lt : list):

    # 각 건물에서 볼 수 있는 건물들의 2차원 배열
    can_see = [[0] * n for _ in range(n)]

    for i in range(n):
        # 기준 빌딩에서 어떤 빌딩까지의 최대 기울기보다 큰 기울기인 빌딩이 있다면 볼 수 있다.
        current_slope = 0
        high_slope = -1000000000
        for j in range(i + 1, n):
            current_slope = (lt[i] - lt[j]) / (i - j)
            if current_slope > high_slope:
                can_see[i][j] = 1
                can_see[j][i] = 1
                high_slope = current_slope

    # 볼 수 있는 건물의 개수 세기
    ans = 0
    for i in can_see:
        ans = max(ans, sum(i))

    print(ans)
            


if __name__ == '__main__':
    n = int(input())
    building = list(map(int, input().split()))
    _1027(n ,building)
