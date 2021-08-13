# 5710번  전기 요금 골드 5

# 두 사람의 총 사용량을 구함
def calculate_electricity_usage(wh):
  if wh <= 200:
    return wh // 2
  if wh <= 29900:
    return (wh - 200) // 3 + 100
  if wh <= 4979900:
    return (wh - 29900) // 5 + 10000
  return (wh - 4979900) // 7 + 1000000

# 사용량에 따른 전기 요금을 구함
def electricity_bill_calculation(wh):
  if wh < 100:
    return wh * 2
  if wh < 10000:
    return (wh - 100) * 3 + 200
  if wh < 1000000:
    return (wh - 10000) * 5 + 29900
  return (wh - 1000000) * 7 + 4979900

# 이진 탐색 소스코드 구현(반복문)
def binary_sharch(target, start, end, total_wh):
  while True:
    person_wh = (start + end) // 2
    neighbor_wh = total_wh - person_wh
    
    diff = electricity_bill_calculation(neighbor_wh) - electricity_bill_calculation(person_wh)

    # 찾은 경우 상근이의 전기 요금 반환
    if diff == target:
      return electricity_bill_calculation(person_wh)
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
    elif diff > target:
      start = person_wh + 1
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 왼쪽 확인
    else:
      end = person_wh - 1

a, b = map(int, input().split())

# 이진 탐색 수행 결과 출력
while a + b != 0:
  # 두 사람의 총 사용량 구함
  total_wh = calculate_electricity_usage(a)
  
  # 상근이의 전기 요금 구함
  print(binary_sharch(b, 1, total_wh, total_wh))

  # 다시 입력받음
  a, b = map(int, input().split())
