from sys import stdin
input = stdin.readline

# -기준으로 다음 -나올 때까지 다 더한 결과들을 모두 빼면 됨
def _1541(expression : list):
    ans = sum(map(int, expression.pop(0).split('+')))
    for i in expression:
        ans -= sum(map(int, i.split('+')))
    
    return ans

if __name__ == "__main__":
    expression = input().strip().split('-')
    print(_1541(expression))
