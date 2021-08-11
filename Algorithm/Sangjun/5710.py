def price_to_watt(p):
    if p > 4979900:
        return 1000000 + (p - 4979900) // 7
    elif p > 29900:
        return 10000 + (p - 29900) // 5
    elif p > 200:
        return 100 + (p - 200) // 3
    else:
        return p // 2

def watt_to_price(wh):
    if wh > 1000000:
        return 4979900 + 7 * (wh - 1000000)
    elif wh > 10000:
        return 29900 + 5 * (wh - 10000)
    elif wh > 100:
        return 200 + 3 * (wh - 100)
    else:
        return wh * 2
    

while True:
    x, y = map(int, input().split())
    if x == y == 0:
        break
    
    total_use = price_to_watt(x)
    srt, end = 0, total_use
    
    # 이분 탐색
    while True:
        # p1 상근, p2 이웃
        p1 = (srt + end) // 2
        p2 = total_use - p1
        diff = abs(watt_to_price(p1) - watt_to_price(p2))

        if diff == y:
            print(watt_to_price(p1))
            break
        elif diff > y:
            srt = p1 + 1
        else:
            end = p1 - 1
