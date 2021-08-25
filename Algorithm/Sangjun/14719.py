from sys import stdin
input = stdin.readline

def _14719(W : int, block : list):
    water = 0
    # 현재 블록 기준으로 왼쪽, 오른쪽 각각 가장 큰 블록 찾아 그 중에 작은 블록과 현재 블록의 높이 차이를 구한다.
    for curr in range(W):
        left, right = max(block[:curr + 1]), max(block[curr:])
        lower = min(left, right)
        water += abs(block[curr] - lower)
    return water

if __name__ == '__main__':
    H, W = map(int, input().split())
    block = list(map(int, input().split()))
    print(_14719(W, block))

    
