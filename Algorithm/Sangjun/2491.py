from sys import stdin
input = stdin.readline

def _2491(N : int, num : list):
    # 최대길이, 오름차순 길이, 내림차순 길이 설정
    max_len = 1
    ascent = 1
    descent = 1
    
    for i in range(N - 1):
        
        # 내림차순일 경우 오름차순 길이 초기화 후 내림차순 1 증가, 최대길이 계산
        if num[i] > num[i + 1]:
            ascent = 1
            descent += 1
            max_len = max(max_len, descent)
        
        # 오름차순일 경우 내림차순과 같이 계산
        elif num[i] < num[i + 1]:
            descent = 1
            ascent += 1
            max_len = max(max_len, ascent)
        
        # 같을 경우 내림차순, 오름차순이 바뀌어도 계산할 수 있도록, 오름차순 내림차순 모두 증가
        else:
            ascent += 1
            descent += 1
            max_len = max(max_len, ascent, descent)
    
    print(max_len)


if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split()))
    _2491(N, num)
