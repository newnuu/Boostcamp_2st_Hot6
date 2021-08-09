# 9204번 체스 골드 5

t = int(input())
chess = []
# data = [[0] * 8 for _ in range(8)]
alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
reverse_alphabet = dict(map(reversed, alphabet.items()))

for i in range(4):
  # 검정 == 0, 흰색 == 1
  chess.append([0, 1, 0, 1, 0, 1, 0, 1])
  chess.append([1, 0, 1, 0, 1, 0, 1, 0])

def fun(x, num_x, y, num_y):
  result = ''

  if chess[x][num_x] != chess[y][num_y]: # 체스판의 색이 다른 경우
    result = 'Impossible'

  elif x == y and num_x == num_y: # x와 y가 같은 경우
    x = reverse_alphabet.get(x)
    result = f'0 {x} {str(num_x + 1)}'

  else: # 체스판의 색이 같은 경우
    start = x + num_x
    end = y + num_y
    num = abs((start - end) // 2)

    # 사선 번호가 작은 쪽
    plus_x = x + num
    plus_y = num_x + num
    # 사선 번호가 큰 쪽
    minus_x = y - num
    minus_y = num_y - num
    # 알파벳 출력
    x = reverse_alphabet.get(x)
    y = reverse_alphabet.get(y)

    # 체스판을 벗어나지 않아야 함
    if plus_x <= 7 and plus_y <= 7:
      plus_x = reverse_alphabet.get(plus_x)

      if plus_x == y and plus_y == num_y:
        result = f'0 {plus_x} {plus_y + 1}'
      else:
        result = f'2 {x} {num_x + 1} {plus_x} {plus_y + 1} {y} {num_y + 1}'

    elif minus_x >= 0 and minus_y >= 0:
      minus_x = reverse_alphabet.get(minus_x)

      if minus_x == y and minus_y == num_y:
        result = f'0 {minus_x} {minus_y + 1}'
      else:
        result = f'2 {x} {num_x + 1} {minus_x} {minus_y + 1} {y} {num_y + 1}'
      
  return result

for _ in range(t):
  x, num_x, y, num_y = input().split()

  x = alphabet.get(x)
  y = alphabet.get(y)

  print(fun(int(x), int(num_x) - 1, int(y), int(num_y) - 1))
