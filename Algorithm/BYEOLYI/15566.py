# 15566번 | 개구리 1 | 실버 1

n, m = map(int, input().split())
interest, flower = [], []
for _ in range(n):
  interest.append(list(map(int, input().split())))
for _ in range(n):
  flower.append(list(map(int, input().split())))

a, b, t = [], [], []
for _ in range(m):
  sum_a, sum_b, sum_t = list(map(int, input().split()))
  a.append(sum_a)
  b.append(sum_b)
  t.append(sum_t)

result = [0] * (n+1)
d1 = [0, 1, 0, 1]
d2 = [0, 0, 1, 1]

def func():
  for i in range(m):
    if interest[a[i]-1][t[i]-1] == interest[b[i]-1][t[i]-1]:
      # print(11111, interest[a[i]-1][t[i]-1], interest[b[i]-1][t[i]-1])
      for j in range(4):
        num1 = flower[a[i]-1][d1[j]]
        num2 = flower[b[i]-1][d2[j]]
        # print(22222, a[i]-1, b[i]-1, num1, num2)
        if num1+1 == num2 or num1-1 == num2 or num1 == num2+1 or num1 == num2-1:
          result[num1] = a[i]
          result[num2] = b[i]
      #     if a[i] not in result and b[i] not in result:
      #       result[num1] = a[i]
      #       result[num2] = b[i]
      #     elif a[i] in result and result[num1] == a[i]:
      #       result[num1] = a[i]
      #       result[num2] = b[i]
      #     elif b[i] in result and result[num2] == b[i]:
      #       result[num1] = a[i]
      #       result[num2] = b[i]
      #     print(33333, a[i], b[i], result)
      # print('-' * 20)
      # print()
    else:
      return False

  return True

if func():
  print('YES')
  result.pop(0)
  print(*result)
else:
  print('NO')
