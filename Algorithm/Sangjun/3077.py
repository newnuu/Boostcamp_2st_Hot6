from sys import stdin
war_num = int(stdin.readline())
answer1_list = stdin.readline().split()
answer2_list = stdin.readline().split()

# 현우 답에 대한 인덱스 알기위한 dict
idx_dict = {x:y for y, x in enumerate(answer2_list)}

total = war_num * (war_num - 1) // 2
score = total

# 실제 답을 순서에 맞게 모두 탐색
for i in range(war_num):
    for j in range(i + 1, war_num):
      # 실제 답의 인덱스 순서와 현우 답의 인덱스 순서 일치하지 않으면 -1점씩 차감
        war1_idx, war2_idx = idx_dict[answer1_list[i]], idx_dict[answer1_list[j]]
        if war1_idx > war2_idx:
            score -= 1

print(f'{score}/{total}')
