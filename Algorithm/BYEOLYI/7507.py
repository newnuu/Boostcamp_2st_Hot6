# 7507번 | 올림픽 게임 | 실버 2

from sys import stdin

def func():
  m = int(input())
  data = [list(map(int, stdin.readline().split())) for _ in range(m)]
  data.sort(key=lambda x: (x[0], x[2]))
  day, now, result = 0, 0, 0

  for d, s, e in data:
    # 날짜가 현날짜보다 작은 경우
    if day < d:
      now = 0 # 현재시간을 0으로 초기화
      day = d # 날짜를 현 날짜로 업데이트
    # 종료시간보다 다음경기 시작시간이 크거나 같은 경우
    if now <= s:
      result += 1 # 결과값 +1
      now = e # 현재시간를 다음경기 종료시간으로 업데이트

  return result

# 테스트 케이스의 개수 n
n = int(input())

for i in range(n):
  print(f'Scenario #{i+1}:')
  print(func(), "\n")
