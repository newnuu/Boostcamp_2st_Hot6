# 2491번 | 수열 | 실버 3

# 수열의 길이 N
n = int(input())
# N개의 숫자
data = list(map(int, input().split()))
# 최종 결과, 현재의 결과
result, answer = 0, 0

# 연속해서 작아지는 수열
for i in range(1, len(data)):
  if data[i-1] >= data[i]:
    answer += 1
    result = max(result, answer)
  else:
    answer = 0

# 다시 초기화
answer = 0

# 연속해서 커지는 수열
for i in range(1, len(data)):
  if data[i-1] <= data[i]:
    answer += 1
    result = max(result, answer)
  else:
    answer = 0

# 최종 출력(n은 1 이상이므로 최소 1, 본인을 더함)
print(result + 1)
