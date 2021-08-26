# 2729번 | 이진수 덧셈 | 실버 4

t = int(input())

for i in range(t):
  # str형으로 입력받음
  a, b = input().split()

  # 2진수에서 10진수로 변환
  result = int(a, 2) + int(b, 2)
  
  # 10진수에서 2진수로 변환
  print(bin(result)[2:])
