import sys
input = sys.stdin.readline

def solution(N, words):
    answer = 1 
    words.sort()
    for i in range(N - 1):
        if not words[i + 1].startswith(words[i]):
            answer += 1

    return answer

if __name__ == '__main__':
    N = int(input())
    words = [input().strip() for _ in range(N)]
    result = solution(N, words)
    print(result)
