import sys
input = sys.stdin.readline

def solution(N, M, arr):
    answer = 1
    for row in range(N):
        for col in range(M):
            limit = N-row if N-row < M-col else M-col
            for size in range(1, limit):
                if arr[row][col] == arr[row+size][col] == arr[row][col+size] == arr[row+size][col+size]:
                    answer = max(answer, (size+1)**2)

    return answer
    
if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = solution(N, M, arr)
    print(result)
