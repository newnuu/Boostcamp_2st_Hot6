import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input()) # 재료 개수
arr = []

# 신맛 쓴맛 리스트
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 모든 조합을 다 고려하기 위해 combinations 사용
com = []
for i in range(1, N+1):
    com.append(combinations(arr, i))

answer = 1000000000 # 최소값 담을 변수

# iter를 돌면서 각각 조합에 대한 차 구하기
for line in com:
    for each in line:
        sour = 1
        bitter = 0
        for e in each:
            sour *= e[0]
            bitter += e[1]
        # 최소값 찾기
        answer = min(answer, abs(sour - bitter))

print(answer)
