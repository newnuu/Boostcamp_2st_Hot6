from sys import stdin
from itertools import combinations
input = stdin.readline

# 음식의 모든 조합 구한 후 신맛과 쓴맛 계산

def _2961(n : int, list : list):
    com = []
    ans = 1000000000
    # 음식의 모든 조합 구하기
    for i in range(1, n + 1):
        com.extend(combinations(list, i))
    
    # 각 조합에서의 신맛 쓴맛 계산
    for i in com:
        S, B = 1, 0
        for s, b in i:
            S *= s
            B += b
        ans = min(abs(S - B), ans)

    return ans

if __name__ == "__main__":
    n = int(input())
    food = [list(map(int,input().split())) for _ in range(n)]
    print(_2961(n, food))
        
