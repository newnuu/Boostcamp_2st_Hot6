'''
https://www.acmicpc.net/problem/4150
피보나치 수
[풀이]
1. 반복문 사용
'''
n = int(input())
a, b = 0, 1
for _ in range(n):
    a, b = b, a+b
print(a)
