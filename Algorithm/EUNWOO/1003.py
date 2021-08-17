t = int(input())
fib = [(1,0),(0,1)] # (0의 호출수, 1의 호출수)
for i in range(2,41):
    fib.append((fib[i-1][0]+fib[i-2][0],fib[i-1][1]+fib[i-2][1]))
for _ in range(t):
    n = int(input())
    print(*fib[n])
