import collections
c = int(input())
n = int(input())

# 연결 정보 저장
conn = collections.defaultdict(list) 
for _ in range(n):
    i,j = map(int,input().split())
    conn[i].append(j)
    conn[j].append(i)

q = collections.deque()
q.append(1)
answer=[1]
# q에 감염된 컴퓨터 넣고 하나씩 pop해서 연결된 컴퓨터 탐색
while q:
    v = q.popleft()
    for i in conn[v]:
        if i not in answer:
            answer.append(i)
            q.append(i)
            
print(len(answer)-1) # 감염된 컴퓨터 수 - 1( 1번 컴퓨터)
