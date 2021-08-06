n = int(input())
h = list(map(int, input().split())) # 자기보다 큰사람이 왼쪽에 몇명 있는지 정보
ans = [0] * n # [0, 0, ..... , 0] 리스트
for p in range(1, n+1): # p 는 1 ~ n + 1까지
    t = h[p-1] 
    cnt = 0
    for i in range(n):
        # t와 cnt가 일치하고 ans[i] == 0 이면 p 값 ans[i]에 입력
        # t와 cnt가 일치함에도 불구하고 ans[i]가 0이 아니라면 for문을 돌면서 0인곳까지 찾음 
        if cnt == t and ans[i] == 0:
            ans[i] = p
            break
        elif ans[i] == 0:
            cnt += 1
print(*ans)
