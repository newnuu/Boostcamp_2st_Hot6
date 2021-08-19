# 9009번 | 피보나치 | 실버 1

from sys import stdin

t = int(input())
data = [0]
a, b = 1, 1
# 피보나치 수 리스트에 삽입
for i in range(43):
  a, b = b, a + b
  data.append(a)

# 입력한 테스트 데이터(t)의 수만큼 실행
for i in range(t):
  n = int(stdin.readline())
  result = []

  # 최소수의 피보나치 수들을 구하기 위해 큰 수부터 체크
  for j in range(len(data)-1, 0, -1):
    # n보다 피보나치 수가 큰 경우
    if data[j] > n:
      continue

    # 결과값에 피보나치 수 삽입
    result.append(data[j])
    # 주어진 정수에서 피보나치 수 뺄셈
    n -= data[j]
    
  result.sort()
  print(*result)

'''
a, b = 1, 1
for i in range(1, 50):
  a, b = b, a + b
  print(f'{i}번째 피보나치 수 : {a}')
'''
