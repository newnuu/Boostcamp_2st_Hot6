# 9204번 체스 골드 5

t = int(input())
chess = []
# data = [[0] * 8 for _ in range(8)]
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for i in range(4):
  # 검정 == 0, 흰색 == 1
  chess.append([0, 1, 0, 1, 0, 1, 0, 1])
  chess.append([1, 0, 1, 0, 1, 0, 1, 0])

def fun(x, num_x, y, num_y):
  result = ''

  while True:
    if chess[x][num_x] != chess[y][num_y]:
      result = 'Impossible'
      break
    elif x == y and num_x == num_y:
      for i in range(8):
        if x == i:
          x = alphabet[i]
      result = '0 ' + x + ' ' + str(num_x + 1)
      break
    elif chess[x][num_x] == chess[y][num_y]:
      result = '여기 부분 해결이 어렵습니다.'
      break
    
  return result

for _ in range(t):
  x, num_x, y, num_y = input().split()

  for i in range(8):
    if x == alphabet[i]:
      x = i + 1
    if y == alphabet[i]:
      y = i + 1

  print(fun(int(x) - 1 , int(num_x) - 1, int(y) - 1, int(num_y) - 1))
