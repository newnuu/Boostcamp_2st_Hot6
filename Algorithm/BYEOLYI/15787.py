# 15787번 | 기차가 어둠을 헤치고 은하수를 | 실버 2

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
train = [deque([0]*20) for _ in range(n)]

for _ in range(m):
    data = list(map(int,input().split()))

    if data[0] == 1:
        train[data[1]-1][data[2]-1]=1

    elif data[0] == 2:
        train[data[1]-1][data[2]-1]=0

    elif data[0] == 3:
        train[data[1]-1].rotate(1)
        train[data[1]-1][0]=0

    elif data[0] == 4:
        train[data[1]-1].rotate(-1)
        train[data[1]-1][19]=0

result = []

for i in train:
    if i not in result:
        result.append(i)

print(len(result))
