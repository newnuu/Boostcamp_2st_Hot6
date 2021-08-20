# 미리 피보나치 수열 list 만들기
f = [0, 1]
for i in range(2, 50):
    f.append(f[i-2] + f[i - 1])

# 입력값을 넣고 해당 수와 가장 가까운 수를 찾아서 
# 차례로 temp값에 넣고 해당 값을 입력값에서 빼주는걸 반복
# 이후 거꾸로 입력되었으니 sort
def fibonacci(x):
    temp = []
    while x:
        for j in range(50):
            if(f[j] <= x):
                t = f[j]
        x = x - t
        temp.append(t)
        temp.sort()
    for k in temp:
        print(k, end=' ')
    print()

T = int(input()) # Testcase

while T:
    n = int(input())
    fibonacci(n)
    T -= 1
