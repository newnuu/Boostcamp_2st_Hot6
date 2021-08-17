'''
https://www.acmicpc.net/problem/1003
피보나치 함수
[풀이]
1. 각 카운트 역시 피보나치와 동일한 원리
'''
n = int(input())
for _ in range(n):
    m = int(input())
    a, b = [1, 0], [0, 1]
    for _ in range(m):
        a, b = b, list(map(sum, list(zip(a, b))))
    print(*a)
