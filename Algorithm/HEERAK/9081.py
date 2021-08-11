from sys import stdin
input = stdin.readline

def solution(char_list):
    # 문자열 뒤에서부터 비교
    for i in range(len(char_list) - 1, 0, -1):
        # 만약 뒤의 문자열이 앞의 문자열보다 크다면(사전순으로 뒤에 나온다면)
        if char_list[i - 1] < char_list[i]:
            # 기준인 i는 그 앞문자의 index
            i -= 1
            for j in range(len(char_list) - 1, 0, -1):
                # 기준인 i번째 문자보다 큰 j번째 문자를 찾고
                if char_list[i] < char_list[j]:
                    # i번쨰 문자와 j번째 문자를 바꾸면
                    char_list[i], char_list[j] = char_list[j], char_list[i]
                    # i번째 문자까지는 모두 그대로고 i+1번쨰 문자열 부터는 사전순으로 정렬해서 concatenate
                    return char_list[:i + 1] + sorted(char_list[i + 1:])
    return char_list


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        char_list = list(input().strip())
        print(''.join(solution(char_list)))
        
    

