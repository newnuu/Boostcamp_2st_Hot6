# 3182번 | 한동이는 공부가 하기 싫어! | 실버 3

n = int(input())
seniors = list(int(input()) for _ in range(n))
seniors.insert(0, 0) # 0번째 추가
result, result_num = 0, 0 # 방문한 선배가 몇 명인지, 한동이가 물어봐야 할 선배의 번호

for i in range(1, n + 1):
  visited = []
  visited.append(i) # 처음 방문한 선배 추가
  j = seniors[i] # 처음 방문한 선배가 가리키는 사람
  
  while True:
    visited.append(j) # 가리키는 사람 추가
    j = seniors[j] # 가리키는 사람 -> 가리키는 사람

    # 가리키는 사람 -> 가리키는 사람 방문한 선배 중에 있으면 break
    if j in visited:
      
      # 이전의 값이 이번에 방문한 선배 수보다 작으면
      if result < len(visited):
        # 한동이가 물어봐야 할 선배의 번호 저장
        result_num = i
        # 방문한 선배가 몇 명인지 저장
        result = len(visited)
      # 이전 값과 방문한 선배 수가 같으면
      elif result == len(visited):
        # 비교하여 번호가 작은 선배를 저장
        result_num = min(i, result_num)
      break

print(result_num)
