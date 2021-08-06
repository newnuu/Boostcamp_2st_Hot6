people_num = int(input())
memory_list = reversed(input().split())
line_list = []


# 키가 가장 큰 사람부터 자리를 잡아 준다고 생각해보면
# 왼쪽에 있는 자신 보다 큰 사람의 숫자는 그 사람의 줄의 위치 인덱스가 된다.

for idx, val in enumerate(memory_list):
    if val == '0':
        line_list.insert(0, people_num - idx)
    else:
        line_list.insert(int(val), people_num - idx)



# 같은 코드 다른 방법

'''
for val, height in zip(memory_list, range(people_num, 0, -1)):
    if val == '0':
        line_list.insert(0, height)
    else:
        line_list.insert(int(val), height)
'''

ans = ' '.join(map(str, line_list))
print(ans)
