import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 기차, 명령

# 기차 갯수만큼 set()을 만듬
# 중복 제거 위해서
trains = [set([]) for _ in range(N)]

for _ in range(M):
    op = list(map(int, input().split()))
    if op[0] == 1: # 명령 1일때
        # 좌석에 추가, 이미 있다면 set이기 때문에 거름
        trains[op[1]-1].add(op[2]) 
    elif op[0] == 2: # 명령 2일때
        # 좌석에서 하차, dicard 사용했기때문에 비어도 에러 x
        trains[op[1]-1].discard(op[2]) 
    elif op[0] == 3: # 명령 3일때
        # 승객들 모두 뒤로 한칸 이동
        tr = list(trains[op[1]-1]) 
        temp = set()
        for t in tr:
            # 20번째 자리일 경우 continue
            if t + 1 > 20: 
                continue
            temp.add(t+1)
        trains[op[1]-1] = temp
    elif op[0] == 4: # 명령 4일때
        # 승객들 모두 앞으로 한칸 이동
        tr = list(trains[op[1]-1])
        temp = set()
        for t in tr:
            # 0번째 자리일 경우 continue
            if t-1 < 1:
                continue
            temp.add(t - 1)
        trains[op[1]-1] = temp

answer = set()
# 같은 패턴 찾기
for train in trains:
    t = tuple(sorted(train))
    answer.add(t)
print(len(answer))
