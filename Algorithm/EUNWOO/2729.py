t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    s = list('0'+str(a+b))
    
    for i in range(len(s)-1,-1,-1):
        if s[i]=='2': # 2이면 앞자리에 1을 더해주고 현재 자리는 0
            s[i] = '0'
            s[i-1] = str(int(s[i-1])+1)        
        elif s[i]=='3': # 이미 2였는데 뒤에서 하나 더 넘어온 경우
            s[i] = '1' # 하나 넘겨주고 현재자리는 1
            s[i-1] = str(int(s[i-1])+1) 
    print(int(''.join(s)))
