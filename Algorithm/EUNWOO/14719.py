h,w = map(int,input().split())
bl = list(map(int,input().split()))
left = 0
right = w-1
left_max,right_max = bl[left],bl[right]
answer = 0

while left<right:
    left_max,right_max = max(left_max,bl[left]),max(right_max,bl[right])  
    
    # 가장 높은 곳으로 향해가면서 최고높이와 현재 높이의 차이를 더해준다
    if left_max<right_max:
        answer+=left_max - bl[left]
        left+=1
    else:
        answer+=right_max - bl[right]
        right-=1
print(answer)
