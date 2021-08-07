from collections import deque
com_num = int(input())
connected_num = int(input())
connected_com_list = [map(int, input().split()) for _ in range(connected_num)]
 

# 각 컴퓨터가 바이러스에 걸렸는지 확인하기 위한 리스트.
# 1번 컴퓨터는 셀 필요 없으므로 0으로 두어도 상관없음.
check_virus = [0] * com_num
queue = deque()


# 컴퓨터간 연결 그래프
board = [[0] * com_num for _ in range(com_num)]

for i in connected_com_list:
    x, y = i
    board[x - 1][y - 1], board[y - 1][x - 1] = 1, 1

    
# 1번 컴퓨터 부터 시작하기 위한 조건
queue.append(0)


# 그래프를 돌며 탐색. 
while queue:
    # 바이러스가 걸린 컴퓨터들로부터 연결되어있는 컴퓨터 탐색
    x = queue.popleft()
    for idx, val in enumerate(board[x]):
        # 컴퓨터간 연결이 되어있고, 바이러스가 걸려있지 않다면,
        # 바이러스가 걸렸다고 표시해준 후, 큐에 넣고 중복방지하기 위해 두 컴퓨터 사이의
        # 연결이 끊겨졌다고 상태를 바꾸어줌.
        if val == 1 and check_virus[idx] == 0:
            check_virus[idx] = 1
            queue.append(idx)
            board[x][idx], board[idx][x] = 0, 0

print(check_virus.count(1))
