'''
https://www.acmicpc.net/problem/18352
특정 거리의 도시 찾기
[풀이]
1. input이 최대 1,000,000 이므로 readline 호출
2. 단방향 경로를 저장하기 위해 defaultdict 선언
3. 도로가 존재하지 않으면 300,001로 설정
=> 거리 정보 k의 최대가 300,000 이므로
4. x부터 출발해서 각 도착지에 가는 거리는 1씩 증가
=> 만약 x - ed 보다 x - st - ed가 더 가까우면 거리 갱신
=> 갱신될 때 ed를 stack에 다시 append
=> ed가 최단거리이므로 ed에서 출발하는 경로들이 다시 갱신될 가능성이 있으므로
5. 목표는 거리가 k인 도착지를 찾는 것이므로 그 이하까지만 dfs
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
dic = defaultdict(list)
for _ in range(m):
    st, ed = map(int, input().split())
    dic[st].append(ed)
stack = [(x, 0)]
answer = [300001] * (n+1)
answer[x] = 0
while stack:
    st, cost = stack.pop()
    for ed in dic[st]:
        if answer[ed] > cost+1:
            answer[ed] = cost+1
            if cost == k-1:
                continue
            stack.append((ed, cost+1))
result = [idx for idx in range(1, n+1) if answer[idx] == k]
(not result and print(-1)) or print(*result, sep='\n')
