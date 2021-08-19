n = int(input())
ans = []
for _ in range(n):
    ans.append(int(input()))
result=[[] for _ in range(n)]
for i in range(n):
    j = ans[i]-1
    result[i].append(i+1)
    while j+1 not in result[i]:
        result[i].append(j+1)
        j = ans[j]-1
print(result.index(max(result,key = lambda x:len(x)))+1)
