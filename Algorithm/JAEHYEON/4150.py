N = int(input()) # 테스트 데이터

fibo = [0 for _ in range(N + 2)] # N + 1개 list 생성
fibo[1] = 1 # 리스트의 1번에 1 입력

# 피보나치 계산
for i in range(2, N+2):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[i-1]) # 출력
