import sys
input = sys.stdin.readline

max_H = 0 # 가장 큰 높이 저장 변수

H, W = map(int, input().split())
block = list(map(int, input().split()))

# 제일 큰 높이의 index 찾기
for i in range(len(block)):
    if max_H < block[i]:
        max_H = block[i]
        max_index = i

total = 0 # 총합
temp_L = 0
temp_R = 0

# 왼쪽부터 max index 전까지 합
for i in range(max_index + 1):
    if block[i] > temp_L:
        temp_L = block[i]
    total += temp_L

# 오른쪽부터 max index + 1 합
for i in range(W - 1, max_index, - 1):
    if block[i] > temp_R:
        temp_R = block[i]
    total += temp_R

# 총합에서 block 합의 차이
print(total - sum(block))
