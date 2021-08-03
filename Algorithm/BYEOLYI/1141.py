# 1141번 접두사 실버 3
# 잘못 푼 것 같습니다. 점심시간에 다시 작성해서 올리겠습니다!








'''
# 참고자료 https://wikidocs.net/1015#1-add

prefix_x = set(['hello', 'goodbye', 'giant', 'hi'])
prefix_not_x = set(['hello', 'hell', 'giant', 'gig', 'g'])

n = int(input())
s = set([])

for i in range(n):
  s.add(input())

result = prefix_x & s # 교집합 prefix_x.intersection(s)
print(result)

result = result - prefix_not_x # 차집합 result.difference(prefix_not_x)
print(result)

print(len(result))
'''
