n = int(input())

# fr 친구관계 0과 1로 표시
fr = [[0 for _ in range(n)] for _ in range(n)]
for r in range(n):
    for i,c in enumerate(input()):
        if  c =="N":
            fr[r][i] = 0
        else:
            fr[r][i]=1

#fr2 : 친구의 친구 관계 (한다리 건너서 친구)- 행렬곱 구현
fr2 = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            fr2[i][j] +=fr[i][k]*fr[k][j] 

# 바로 친구이거나 한다리 건너 친구인 경우 - 각각 친구 집합 만들기      
answer = [set() for _ in range(n)]
for r in range(n):
    for c in range(n):
        if r!=c and fr[r][c]>=1:
            answer[r].add(c)
        if r!=c and fr2[r][c]>=1:
            answer[r].add(c)

# 가장 긴 친구집합의 길이 출력
print(len(max(answer,key = lambda x :len(x))))
