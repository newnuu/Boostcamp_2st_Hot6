import sys
input = sys.stdin.readline

def solution(word):
    for i in range(len(word)-1, 0, -1): # 마지막 문자들 부터 비교
        if word[i-1] < word[i]: # word[i-1]이 변경점
            order = sorted(list(word[i-1:])) 
            for c in order: # word[i-1] 보다 큰 최소의 문자를 찾는다.
                if word[i-1] < c:
                    order.remove(c) # word[i-1]을 대체할 문자 'c'를 한개 제거
                    return word[:i-1] + c + ''.join(order)

    return word

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        word = input().strip()
        result = solution(word)
        print(result)
