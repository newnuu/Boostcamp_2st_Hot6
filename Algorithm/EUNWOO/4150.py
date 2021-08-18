n = int(input())
fib = [0]+[1 for _ in range(n)]
for i in range(3,n+1):
    fib[i] = fib[i-1]+fib[i-2]
print(fib[n])
