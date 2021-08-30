'''
https://www.acmicpc.net/problem/15566
개구리 1
[풀이]
1. 입력
=> fun : 주제에 대한 흥미도
=> pref : 개구리가 선호하는 연꽃의 번호
=> subject : 통나무의 주제
2. pref를 기준으로 개구리들이 배치될 수 있는 모든 경우의 수를 구한다.
=> 처음 연꽃은 0으로 초기화되어있다
=> if case[p] == 0 : 연꽃 자리가 비어있을 때
=> if p == pref[idx][1] : 선호하는 자리가 한개일 때
=> 각 연꽃 자리를 선호하는 개구리의 인덱스로 설정된다.
3. 연꽃에 앉은 개구리들의 fun을 비교
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
fun = [list(map(int, input().strip().split())) for _ in range(N)]
pref = [list(map(int, input().strip().split())) for _ in range(N)]
subject = [list(map(int, input().strip().split())) for _ in range(M)]

cases = [[0] * (N+1)]
for idx in range(N):
    temp = []
    while cases:
        case = cases.pop()
        for p in pref[idx]:
            if case[p] == 0:
                temp.append(case[:p]+[idx+1]+case[p+1:])
            if p == pref[idx][1]:
                break
    cases.extend(list(temp))

for case in cases:
    for a, b, t in subject:
        if fun[case[a]-1][t-1] != fun[case[b]-1][t-1]:
            break
    else:
        print("YES")
        print(*case[1:])
        break
else:
    print("NO")
