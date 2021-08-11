import sys
input = sys.stdin.readline

# 앞으로 나올 사람은 항상 현재 사람 보다 크기 때문에, 빈공간을 n개 지나친 후에 다음 빈공간에 위치하면 된다.
def solution(N, arr):
    answer = [None] * N

    for i, n in enumerate(arr):
        cnt = idx = 0

        while True:
            if answer[idx] == None: # 빈 공간 
                if cnt == n: # 지나온 None의 개수가 n인 경우, 현재 공간에 삽입 
                    break
                cnt += 1 # 빈 공간++
            idx += 1

        answer[idx] = str(i + 1)

    return ' '.join(answer)


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    result = solution(N, arr)
    print(result)
