import itertools

n = int(input())
t = []
c=[]
diff=[]

for i in range(1,n+1):
    t.append(list(map(int,input().split())))
    c+=list(itertools.combinations(range(n),i)) # 모든 경우의 수 (인덱스)

for i in c: # 모든 경우의 수에 대해
    m,sm = 1,0
    for j in range(len(i)): # 각 인덱스에 해당하는 곱셈, 덧셈값 계산 
        s,b = t[i[j]]
        m*=s
        sm+=b
    diff.append(abs(m-sm))
    
print(min(diff)) 
