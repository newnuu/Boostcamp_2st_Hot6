import sys
input = sys.stdin.readline

def solution(N):
    D = [0] * (N + 1) # dp table
    D[0], D[1],  = (1, 0), (0, 1) # 초기값
    for i in range(2, N): # dp
        D[i] = (D[i-1][0] + D[i-2][0], D[i-1][1] + D[i-2][1])

    return D

if __name__ == '__main__':
    T = int(input())
    N = [int(input()) for _ in range(T)]
    result = solution(41) # 최대 경우의 dp table 생성
    for n in N: # 각 테스트
        print(*result[n]) 
