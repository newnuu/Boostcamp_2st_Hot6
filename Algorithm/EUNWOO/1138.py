n = int(input())
line = list(map(int,input().split()))
answer = [len(line)]

for i in range(len(line)-2,-1,-1):
    answer = answer[:line[i]]+[i+1]+answer[line[i]:]
for i in answer:
    print(i,end=' ')
