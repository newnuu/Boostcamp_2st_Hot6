from sys import stdin
input = stdin.readline

def _2491(N : int, num : list):
    max_len = 1
    ascent = 1
    descent = 1

    for i in range(N - 1):
        if num[i] > num[i + 1]:
            ascent = 1
            descent += 1
            max_len = max(max_len, descent)
        elif num[i] < num[i + 1]:
            descent = 1
            ascent += 1
            max_len = max(max_len, ascent)
        else:
            ascent += 1
            descent += 1
            max_len = max(max_len, ascent, descent)
    
    print(max_len)


if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split()))
    _2491(N, num)
