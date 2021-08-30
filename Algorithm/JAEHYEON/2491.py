import sys
input = sys.stdin.readline

N = int(input()) # 수열의 길이
seq_list = list(map(int, input().split())) # 수열 리스트

cnt = 1
max_length = 1

#점점 작아지는 수열 찾기
for i in range(1, N):
    if seq_list[i - 1] >= seq_list[i]:
        cnt += 1
    else:
        cnt = 1
    if max_length <= cnt:
        max_length = cnt

cnt = 1
# 점점 커지는 수열 찾기
for i in range(1, N):
    if seq_list[i - 1] <= seq_list[i]:
        cnt += 1
    else:
        cnt = 1
    if max_length < cnt:
        max_length = cnt

print(max_length)
