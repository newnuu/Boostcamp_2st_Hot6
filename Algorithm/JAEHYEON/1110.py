# https://www.acmicpc.net/problem/1110

N = int(input())
copy_N = N # 입력 변수 Copy
temp = 0
temp_1 = 0
cnt = 0
while True:
  # 입력받은 변수의 각 자리수 더해주기
  temp = N // 10 + N % 10
  # 각 자리수를 더해 나온 값의 1의자리 숫자와 
  # 원래 값의 1의자리숫자에 10의 곱하고 
  # 위 temp값의 1의 자리 숫자를 더하여 새로운 수 만들기
  temp_1 = (N % 10) * 10 + temp % 10 
  cnt += 1
  N = temp_1
  # Copy된 입력값과 새로만든 수를 비교
  if copy_N == temp_1: 
    break
print(cnt)
