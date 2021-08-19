import sys
input = sys.stdin.readline

def solution(m, matches):
    answer = 1
    matches.sort(key=lambda x : (x[0], x[2])) # day, end time으로 정렬
    d, s, e = matches[0] # day, start, end
    for i in range(1, m):
        if d != matches[i][0] or e <= matches[i][1]: # 다음 경기 참석 가능
            d, s, e = matches[i] # day, start, end 갱신
            answer += 1

    return answer

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        m = int(input())
        matches = [tuple(map(int, input().split())) for _ in range(m)]
        result = solution(m, matches)
        print(f'Scenario #{t + 1}:\n{result}\n')
