import sys
input = sys.stdin.readline

n,m = map(int, input().split())
cmd = []
train=[[0 for _ in range(21)] for _ in range(n+1)]
crossed = []
cnt=0

for _ in range(m):
    cmd.append(list(map(int,input().split())))
    c = cmd[-1][0] # 명령 번호
    tn = cmd[-1][1] # 기차 번호
    if c==1:
        if train[tn][cmd[-1][2]]==0:
            train[tn][cmd[-1][2]]=1
    elif c==2:
        if train[tn][cmd[-1][2]]==1:
             train[tn][cmd[-1][2]]=0
    elif c==3:
        for j in range(20,0,-1):
            if j==20: # 마지막 자리에 사람있는 경우 하차
                train[tn][j]=0 
            if train[tn][j]==1:
                train[tn][j+1]=1
                train[tn][j]=0         
    elif c==4:
        for j in range(1,21):
            if train[tn][j]==1:
                train[tn][j-1]=1
                train[tn][j]=0
                
for t in range(1,len(train)):
    train[t][0]=0 # 첫번째 자리에 1이 있는 경우 4번 명령을 하면 인덱스 0에 1이 들어가므로 인덱스 0은 모두 0으로 바꿔준다
    if train[t] in crossed: # 같은 배열 이미 지나간 경우
        continue
    else: 
        cnt+=1
        crossed.append(train[t])
        
print(cnt)
