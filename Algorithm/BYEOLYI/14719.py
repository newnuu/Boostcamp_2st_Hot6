# 14719번 | 빗물 | 골드 5

# 세로 길이 H, 가로 길이 W
h, w = map(int, input().split())
# 블록이 쌓인 높이
block = list(map(int, input().split()))
# 결과값
result = 0

# 1번째 블록과 w번째 블록은 빗물이 고일 수 없음
for i in range(1, w - 1):
  left = max(block[:i])
  right = max(block[i+1:])
  # 더 낮은 높이까지 빗물이 고일 수 있기 때문
  rain = min(left, right)

  # 현재 높이보다 벽이 더 높은 경우
  if rain > block[i]:
    # 양쪽의 벽 - 현재 높이 = 해당 높이에서 고이는 빗물
    result += rain - block[i]

  # print(left, right, rain, block[i], result)

print(result)



'''
# 삽질....

def func():
  # 2차원 세계의 세로 길이 H, 2차원 세계의 가로 길이 W
  h, w = map(int, input().split())
  # 블록이 쌓인 높이
  block = list(map(int, input().split()))
  # 왼쪽 가장 높은 블록, 고이는 빗물 블록중에 가장 높은 블록, 고이는 빗물이 있는 블록의 수, 고이는 빗물이 있는 블록의 높이, 최종 결과값
  left, h_max, num, rain, result = block[0], 0, 0, 0, 0

  for i in range(1, w):
    # 왼쪽 블럭 길이 > 오른쪽 블록 길이
    if left > block[i]:
      # 마지막 블럭이고 고이는 빗물이 있는 블록이 있는 경우
      if i == w-1 and num >= 1 and block[i] > h_max:
        # 결과값 += 블록의 수 * 마지막 블록 - 블록의 높이
        result += num * block[i] - rain

      if num >= 1:
        result += num * block[i] - rain
        left, h_max, num, rain = block[i], 0, 0, 0
      else:
        h_max = max(h_max, block[i])
        num += 1
        rain += block[i]

    # 왼쪽 블럭 길이 == 오른쪽 블록 길이
    elif left == block[i]:
      if num >= 1:
        result += num * left - rain
        left, h_max, num, rain = block[i], 0, 0, 0

    # 왼쪽 블럭 길이 < 오른쪽 블록 길이
    else:
      # 고이는 빗물이 있는 블록이 있는 경우
      if num >= 1:
        result += num * left - rain
        left, h_max, num, rain = block[i], 0, 0, 0
      else:
        left = block[i]

    # print('\n left, h_max, num, rain, result')
    # print(left, h_max, num, rain, result)
  
  return result

print(func())
'''
