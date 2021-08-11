# 1058번 친구 실버 2

n = int(input())
data = []
visit = []
result = 0

for i in range(n):
  data.append(list(input()))

for i in range(n):
  visit.append([0] * n)

for k in range(n):
  for i in range(n):
    for j in range(n):
      # A와 A는 친구가 아니기 때문
      if i == j:
        continue # 반복문 나감

      # 두 사람이 친구일 경우
      if data[i][j] == 'Y':
        visit[i][j] = 1
      
      # A와 친구이고, B와 친구인 C가 존재할 경우
      elif data[i][k] == 'Y' and data[k][j] == 'Y':
        visit[i][j] = 1

for i in visit:
  result = max(result, sum(i))

print(result)
