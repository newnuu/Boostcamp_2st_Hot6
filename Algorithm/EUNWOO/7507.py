
import sys
n = int(input())

for i in range(n):
    print("Scenario #"+str(i+1)+":")
    sc = []
    m = int(sys.stdin.readline())
    
    for j in range(m):
        sc.append(sys.stdin.readline().split()) 
        
    sc.sort(key = lambda x :(x[0],x[2])) # 날짜순, 끝나는 시간순 정렬
    d,s,e = sc[0]
    ans=1
    
    for l in range(1,len(sc)):
        if sc[l][0]==d and sc[l][1]<e: # 날짜가 바뀌거나 뒤의 시작시간이 끝나는시간보다 빠르면 continue
            continue
        else:
            ans+=1
            d,s,e = sc[l]
            
    print(ans)
    print()
