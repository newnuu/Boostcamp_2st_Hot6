import sys
input = sys.stdin.readline


def get_wh_from_bill(bill):
    #총 전기 사용량 체크를 위한 list
    arr = [100 * 2, 100 * 2 + 9900 * 3, 100 * 2 + 9900 * 3 + 990000 * 5]

    if bill <= arr[0]: # 두사람의 총 전기 사용량이 100 * 2 보다 작을경우
        return bill // 2
    if bill <= arr[1]: # 100 * 2 + 9900 * 3 보다 작을경우
        return 100 + (bill - arr[0]) // 3
    if bill <= arr[2]: # 100 * 2 + 9900 * 3 + 990000 * 5 보다 작을경우
        return 10000 + (bill - arr[1]) // 5

    return 1000000 + (bill - arr[2]) // 7 # 나머지


def get_bill_from_wh(wh):
    arr = [100, 10000, 1000000]

    if wh < arr[0]:
        return wh * 2
    if wh < arr[1]:
        return 100 * 2 + (wh - 100) * 3
    if wh < arr[2]:
        return 100 * 2 + 9900 * 3 + (wh - 10000) * 5
    return 100 * 2 + 9900 * 3 + 990000 * 5 + (wh - 1000000) * 7


#상근이의 전기사용량을 구하기 위한 이진탐색
def binary_search(start, end, target):
    total_wh = end  # 상근과 이웃의 총 전기사용량

    while True:
        my_wh = (start + end) // 2  # 상근이 전기사용량
        your_wh = total_wh - my_wh  # 이웃 전기사용량

        #각각에 대한 전기 사용량을 구하고 빼줌으로서 diff 값 얻음
        diff = get_bill_from_wh(your_wh) - get_bill_from_wh(my_wh)

        if diff == B: # diff 값이 B와 같다면 return
            return get_bill_from_wh(my_wh)

        if diff > B: # B보다 크다면 start 증가
            start = my_wh + 1
        else: # B보다 작다면 end 감소
            end = my_wh - 1


while True:
    A, B = map(int, input().split())

    # 종료 조건
    if A == 0 and B == 0:
        break

    # 총 전기 사용량 구하기
    wh = get_wh_from_bill(A)

    # 상근이의 전기 사용량 구하기
    print(binary_search(1, wh, B))
