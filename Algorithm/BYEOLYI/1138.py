# 1138  한 줄로 서기  실버 2

n = int(input())
height = list(map(int, input().split()))
result = [0] * n
# print(n, height, result)

for i in range(1, n+1): 
  t = height[i - 1]
  cnt = 0
  for j in range(n):
    if cnt == t and result[j] == 0:
      result[j] = i
      break
    elif result[j] == 0:
      cnt += 1
  # print(t, cnt, result[j])

print(result)

'''
n = int(input())
height = list(map(int, input().split()))
result = [0] * n
print(n, result, height)

for i in range(n):
  print(result[height[i]], height[i])
  if result[height[i]] == 0:
    result[height[i]] = str(i + 1)
  else:
    for j in range(n):
      if result[height[i - 1]] < result[height[i]]:
        if result[height[i] + j] == 0:
          result[height[i] + j] = str(i + 1)
          break
      else
  print(result)

result = " ".join(rsult)
print(result)
'''
