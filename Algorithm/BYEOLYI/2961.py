# 2961번 | 도영이가 만든 맛있는 음식 | 실버 1

n = int(input())
sour, bitter = [], []
result = 1e9

for i in range(n):
  s, b = map(int, input().split())
  sour.append(s)
  bitter.append(b)

def func(idx, start, s, b):
  global result
  if idx == target:
    if abs(s-b) < result:
      result = abs(s-b)
    return
  
  for i in range(start, n):
    func(idx+1, i+1, s*sour[i], b+bitter[i])

for target in range(1, n+1):
  func(0, 0, 1, 0)

print(result)
