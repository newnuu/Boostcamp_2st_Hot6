T = int(input()) # Testcase

# fibonacci(0, 1, 2) 일때의 0과 1의 갯수를 미리 저장
zero = [1, 0, 1]
one = [0, 1, 1]

def dp(N):
    #원하고자 하는 N값이 zero(or one) 의 크기 즉, 3보다 크다면
    if len(zero) <= N:
        for i in range(len(zero), N+1):
            # i - 1 값과 i - 2 값 더해서 append
            zero.append(zero[i-1]+zero[i-2]) 
            one.append(one[i-1]+one[i-2])
    print(f'{zero[N]} {one[N]}')

while T:
    N = int(input())
    dp(N)
    T -= 1
