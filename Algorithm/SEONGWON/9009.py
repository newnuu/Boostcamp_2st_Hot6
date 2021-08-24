import sys
input = sys.stdin.readline

def solution(n, fibos):
    answer = []
    for i in range(len(fibos)-1, 0, -1): # greedy
        if fibos[i] <= n: # n보다 작거나 같은 수 append
            answer.append(fibos[i])
            n -= fibos[i] # 더해진 fibos[i]만큼 차감
            if n == 0: break

    return answer[::-1]

def get_fibo(): # 필요한 만큼 fibo 수열 get
    answer = [0, 1]
    while answer[-1] <= 1000000000:
        answer.append(answer[-2] + answer[-1])

    return answer

if __name__ == '__main__':
    T = int(input())
    fibos = get_fibo()
    for _ in range(T):
        n = int(input())
        result = solution(n, fibos)
        print(*result)
