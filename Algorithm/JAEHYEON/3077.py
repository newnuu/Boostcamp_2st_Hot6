N = int(input()) # 해전의 개수
word = input().split() # 현우가 작성한 답안
dic_word = {values : index for index, values in enumerate(word)} # key value 바꿈, 현우 답안 dic
answer = input().split() # 진짜 답안
cnt = 0 # 점수 count

# 2중 for loop를 이용하여 뒤에 오는 값의 dic value 값이 작다면 count 1 증가
for i in range(N):
    for j in range(i+1, N):
        if dic_word[answer[i]] < dic_word[answer[j]]:
            cnt += 1

print(f'{cnt}/{(N * (N-1)) // 2}')
