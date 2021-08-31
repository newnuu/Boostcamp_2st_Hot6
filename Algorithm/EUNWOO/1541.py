s = input().split('-') # -로 분리
sl = [sum(list(map(int,i.split('+')))) for i in s] # 분리된 수들은 모두 각각 더한다
print(sl[0]-sum(sl[1:])) # 첫번째 숫자만 + 나머지는 모두 -
