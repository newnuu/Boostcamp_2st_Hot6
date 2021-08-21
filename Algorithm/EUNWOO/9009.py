import sys
s = []
fib = [0,1]
t = int(sys.stdin.readline())

for _ in range(t):
    s.append(int(sys.stdin.readline()))
    
for n in s:
    ans=[]
    while fib[-1]<n: # 현재 수가 될 때까지 피보나치
        fib.append(fib[-1]+fib[-2])
        
    for i in range(len(fib)-1,-1,-1):
        if fib[i]>n: #현재 수보다 크면 continue
            continue
        elif n-fib[i]>=0: # 현재수에서 뺄 수 있는 큰 수부터 빼기
            ans.append(fib[i])
            n -= fib[i]
    ans=sorted(ans[:-1])# 마지막 0 제거, 정렬 
    print(*ans)
