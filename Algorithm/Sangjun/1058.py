num = int(input())
friends = [list(input()) for _ in range(num)]
board = [[0 for _ in range(num)] for _ in range(num)]

for i in range(num):
    for j in range(num):
        for k in range(num):
            # 자기자신과는 친구가 아니므로 패스
            if j == k:
                continue
            
            # 두 사람이 친구이거나 친구가 아닐 경우 2-친구를 찾음
            if friends[j][k] == 'Y' or (friends[i][k] == 'Y' and friends[j][k] == 'Y'):
                board[j][k] = 1


# 2-친구가 가장 많은사람 찾기
max_2_friends = 0

for i in board:
    max_2_friends = max(max_2_friends, sum(i))

print(max_2_friends)
    
