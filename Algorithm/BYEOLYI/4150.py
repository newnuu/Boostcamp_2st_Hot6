# 4150번 | 피보나치 수 | 실버 4

def fibonacci(n):
  # f(1) = 1, f(2) = 1
  if n == 1 or n == 2:
    return 1
  
  # f(n > 2) = f(n − 1) + f(n − 2)
  a, b = 1, 1
  for _ in range(1, n):
    a, b = b, a+b
    # print(a, b)

  return a
  
n = int(input())
print(fibonacci(n))

'''
# 재귀함수 : 런타임 에러
def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  elif n > 2:
    return fibonacci(n-1) + fibonacci(n-2)
  
n = int(input())
print(fibonacci(n))
'''
