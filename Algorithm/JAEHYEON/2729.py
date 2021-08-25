import sys
input = sys.stdin.readline

T = int(input()) # Testcase

for _ in range(T):
    nums = [int(e, 2) for e in input().split()] # 2진수 10진수 변환
    # 10진수에서 합 구하고 다시 2진수로 변환
    # 앞에 0b 가 붙기때문에 제외하고 출력
    print(bin(sum(nums))[2:])
