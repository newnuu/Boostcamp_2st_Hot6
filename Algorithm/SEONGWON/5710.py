import sys
input = sys.stdin.readline

def solution(A, B):
    whs = [0, 100, 10000, 1000000, float('inf')]
    fees = [2, 3, 5, 7]
    tot_fees = [100 * 2, 9900 * 3, 990000 * 5, float('inf')]

    def money_to_wh(money): # 요금 -> 전기 사용량
        for i in range(len(tot_fees)):
            if money < sum(tot_fees[:i+1]):
                return whs[i] + (money - sum(tot_fees[:i])) / fees[i]

    def wh_to_money(wh): # 전기 사용량 -> 요금
        for i in range(len(whs)):
            if wh < whs[i]:
                return sum(tot_fees[:i-1]) + (wh - whs[i-1]) * fees[i-1]

    mn, mx = 1, 10**9
    while mn < mx - 1: # 이분 탐색
        mid = (mn + mx) // 2
        if wh_to_money(money_to_wh(mid) + money_to_wh(mid + B)) <= A:
            mn = mid
        else:
            mx = mid

    return mn

if __name__ == '__main__':
    while True:
        A, B = map(int, input().split())
        if A == B == 0:
            break
        result = solution(A, B)
        print(result)
