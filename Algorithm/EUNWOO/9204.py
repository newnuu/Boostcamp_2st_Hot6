import collections
t = int(input())

for _ in range(t):
    x1,y1,x2,y2 = input().split()
    
    # 같은 색이 아니면 Impossible
    if (ord(x2)-ord(x1))%2!= (int(y2)-int(y1))%2:
        print("Impossible")
        continue
        
    else: # 같은 색이면
      
        # 출발지와 도착지 같은 경우
        if x1==x2 and y1==y2:
            print(0,x1,y1)
            continue
            
        # 같은 직선 위에 있는 경우
        elif abs(ord(x1)-ord(x2))==abs(int(y1)-int(y2)):
            print(1,x1,y1,x2,y2)
            continue
        
        # 숫자 좌표로 변환
        c = ord(x1)-ord('A')
        r = ord(x2)-ord('A')
        
        l1=set()
        l2 = set()
        
        # 출발지에서 움직일 수 있는 모든 좌표 구하기
        for i in range(7-c):
            if int(y1)+i <=8:
                l1.add((c+i,int(y1)+i))
            if int(y1)-i >0:    
                l1.add((c+i,int(y1)-i))
        for i in range(1,c+1):
            if int(y1)-i >0:
                l1.add((c-i,int(y1)-i))
            if int(y1)+i <=8:
                l1.add((c-i,int(y1)+i))
        
        # 도착지에서 움직일 수 있는 모든 좌표 구하기
        for i in range(0,7-r):
            if int(y2)+i <=8:
                l2.add((r+i,int(y2)+i))
            if int(y2)-i >0:    
                l2.add((r+i,int(y2)-i))
        for i in range(1,r+1):
            if int(y2)-i >0:
                l2.add((r-i,int(y2)-i))
            if int(y2)+i <=8:
                l2.add((r-i,int(y2)+i))
        
        # 츌발지와 도착지에서 모두 갈 수 있는 좌표 
        inter = list(l1.intersection(l2))[0]
        
        # 출발지, 교차점, 도착지 출력
        print(2,x1,y1,chr(inter[0]+ord('A')),inter[1],x2,y2)
