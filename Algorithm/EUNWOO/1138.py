n = int(input())
line = list(map(int,input().split()))
answer = [len(line)]

# 뒤에서부터 
for i in range(len(line)-2,-1,-1):
    answer = answer[:line[i]]+[i+1]+answer[line[i]:] # 앞에 큰 사람이 있는 수대로 앞에서부터 잘라서 중간에 넣기
for i in answer:
    print(i,end=' ')
