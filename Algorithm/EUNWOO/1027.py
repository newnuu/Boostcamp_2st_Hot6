n = int(input())
bd = list(map(int,input().split()))
result = [0 for _ in range(n)]

# i 기준 왼쪽에 볼 수 있는 건물
for i in range(1,n):
    ml = max(bd[:i])
    s=float(bd[i]-bd[i-1])
    result[i]+=1 # 바로 이전 건물은 볼 수 있음
    for l in range(i-2,-1,-1): # 전전 건물 부터 첫번째 건물까지 거꾸로
        sl = (bd[i]-bd[l])/(i-l)
        if s<=0: # 전의 기울기가 - 인경우
            if sl<s: # 둘다 - 인 경우 앞의 건물과의 기울기가 더 작아야한다
                result[i]+=1
                s = sl
        elif sl<0: # 전의 기울기는 +, 현재의 기울기는 - 이면 항상 볼 수 있다
            result[i]+=1
            s=sl
        elif s > sl: # 전의 기울기도 +, 현재의 기울기도 + 이면 전의 기울기가 더 클때 볼 수 있다 (뒤의 건물이 더 낮을 때)
            result[i]+=1
            s=sl
            
# i 기준 오른쪽에 볼 수 있는 건물
for i in range(n-1):
    s = float(bd[i+1]-bd[i])
    result[i]+=1 # 바로 다음 건물을 볼 수 있다
    for r in range(i+2,n):
        sr = (bd[r]-bd[i])/(r-i) # r번째 건물과 기준 건물 사이의 기울기
        if s<0: # 현재의 기울기가 - (기준 건물보다 낮으면) 
            if sr>=0: #다음 건물의 기울기가 + 이면(기준 건물보다 높음) 항상 볼 수 있다
                result[i]+=1
                s = sr
            elif s<sr: # 둘다 기준 건물보다 낮으면 이전건물보다는 높아야 볼 수 있다
                result[i]+=1
                s = sr            
        elif s<sr: # 이전건물과 현재 건물 모두 기준 건물보다 높으면 이전 건물보다 높아야 볼 수 있다
            result[i]+=1
            s = sr

print(max(result)) 
