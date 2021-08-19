# 두 빌딩간의 기울기
def slope(x1, y1, x2, y2):
    return (y2-y1) / (x2-x1)

N = int(input())
building = list(map(int, input().split()))

result = 0
for i, y1 in enumerate(building):
    x1 = i + 1
    cur_slope_right = None
    right = 0
    #오른쪽으로 볼 수 있는 고층빌딩 탐색
    for j in range(i+1, N+1):
        if j == N:
            break
        x2 = j + 1
        y2 = building[j]
        slope_right = slope(x1, y1, x2, y2)
        #전에 구한 기울기 보다 현재 구한 기울기가 크다면
        if cur_slope_right is None or cur_slope_right < slope_right:
            cur_slope_right = slope_right
            right += 1
    
    cur_slope_left = None
    left = 0
    #왼쪽으로 볼 수 있는 고층빌딩 탐색
    for j in range(i-1, -1, -1):
        if j == -1:
            break
        x2 = j + 1
        y2 = building[j]
        slope_left = slope(x1, y1, x2, y2)
        #전에 구한 기울기 보다 현재 구한 기울기가 작다면
        if cur_slope_left is None or cur_slope_left > slope_left:
            cur_slope_left = slope_left
            left += 1
    
    # 오른쪽에서 볼 수 있는 빌딩수와 왼쪽에서 볼수있는 빌딩수의 합을 구하고
    # result 값 갱신
    if(left+right) > result : 
        result = left + right

print(result)
