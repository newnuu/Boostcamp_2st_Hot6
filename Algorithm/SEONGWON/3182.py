import sys
input = sys.stdin.readline

def solution(N, G):
    counts = [0] * (N + 1) # 각 선배를 시작으로 몇 번 contact가 되는지 저장
    path = [0] * (N + 1) # visited 배열

    def recursive(cur):
        if path[cur] == 1: # cycle 발생
            return 0

        path[cur] = 1 # visit
        cnt = recursive(G[cur]) + 1 # 재귀 호출(다음 선배 연락)
        path[cur] = 0
        return cnt

    for i in range(1, N + 1):
        counts[i] = recursive(i)
    return counts.index(max(counts))

if __name__ == '__main__':
    N = int(input())
    G = {i + 1 : int(input()) for i in range(N)}
    result= solution(N, G)
    print(result)
