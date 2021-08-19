import sys
input = sys.stdin.readline

def solution(N, submit, answer):
    count = total = N * (N - 1) // 2 # 전체 문제 개수

    for s in submit: # 작성한 답안에 따른 해전을 순차적으로 검사
        count -= answer.index(s) # 전체 문제 개수로 초기화 된 count에서 s로 오답 개수 빼기
        answer.remove(s) # s에 대한 검사를 완료 했으므로, 정답지에서 s를 제거

    return str(count) + '/' + str(total)

if __name__ == '__main__':
    N = int(input())
    submit = input().split()
    answer = input().split()
    result = solution(N, submit, answer)
    print(result)
