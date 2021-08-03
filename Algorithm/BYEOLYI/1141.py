# 1141번 접두사 실버 3

n = int(input())
s = []
result = 0

for i in range(n):
  s.append(input())

for i in range(n):
  for j in range(n):
    s1 = s[i]
    s2 = s[j]
  
    if i != j:
      if len(s1) == 1 and s1 == s2[:1]:
        continue
      elif len(s2) == 1 and s1[:1] == s2:
        continue
      elif len(s1) > 0 and len(s2) > 0 and s1[:2] == s2[:2]:
        continue
      else:
        result += 1

print(result // n)
