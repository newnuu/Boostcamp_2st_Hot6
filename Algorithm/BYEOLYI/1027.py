# 1027번 | 고층 건물 | 골드 4

n = int(input())
data = list(map(int, input().split()))
zeros = [0] * n # 해당 층에서 보이는 빌딩 개수 저장

# 2중 for문으로 모든 빌딩 비교
for i in range(n):
  check = -1e9
  for j in range(i + 1, n):
    # 기울기 계산
    slope = (data[j] - data[i]) / (j - i)
    # 빌딩에 가리지 않는 경우
    if slope > check:
      # 최종적으로 i번째에서 기울기가 제일 큰 값 저장
      check = slope
      # 서로 볼 수 있기 때문에 +1
      zeros[i] += 1
      zeros[j] += 1
      
result = 0
# 가장 많은 고층 빌딩이 보이는 빌딩
for i in zeros:
  result = max(result, i)
print(result)
