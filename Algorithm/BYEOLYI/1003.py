# 1003번 | 피보나치 함수 | 실버 3

def fibonacci(n):
  a, b = 1, 1
  # fibonacci(0)은 0을 출력, 0을 리턴
  if n == 0: b = 0
  elif n == 1: a = 0
  
  # 호출횟수 = 피보나치 수
  # f(n > 2) = f(n − 1) + f(n − 2)
  for _ in range(2, n):
    a, b = b, a+b
    # print(a, b)
  return a, b
  
# 테스트 케이스의 개수 T
t = int(input())

for _ in range(t):
  n = int(input())
  a, b = fibonacci(n)
  print(a, b)

'''
# 재귀 함수 시간 초과
def fibonacci(n):
  global count0, count1
  # print(count0, count1)

  if n == 0:
    count0 += 1
    return 0

  elif n == 1:
    count1 += 1
    return 1

  else:
    return fibonacci(n-1) + fibonacci(n-2)

# 테스트 케이스의 개수 T
t = int(input())

for _ in range(t):
  n = int(input())
  count0, count1 = 0, 0
  fibonacci(n)
  print(count0, count1)
'''
