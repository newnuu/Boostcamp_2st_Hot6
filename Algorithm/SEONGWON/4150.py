import sys
input = sys.stdin.readline

def solution(N):
    D = [0] * (N + 1) # dp table
    D[0] = D[1] = 1 # 초기값
    for i in range(2, N): # dp
        D[i] = D[i-1] + D[i-2]

    return D[N-1] # 

if __name__ == '__main__':
    N = int(input())
    result = solution(N)
    print(result)
