'''
https://www.acmicpc.net/problem/1541
잃어버린 괄호
[풀이]
1. 최초의 마이너스 위치를 찾는다.
2. 이 위치 기준으로 양쪽을 각각 더하고 앞에서 뒤를 빼준다.
'''
import sys
input = sys.stdin.readline
exp = input()
idx = exp.find('-')
if idx == -1: a, b = exp, '0'
else: a, b = exp[:idx], exp[idx+1:]
a = list(map(int, a.split('+')))
b = list(map(int, b.replace('-', '+').split('+')))
print(sum(a) - sum(b))
