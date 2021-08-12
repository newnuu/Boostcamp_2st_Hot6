n = int(input())
ans = input().split()
sub = input().split()
result=(n*(n-1))//2
for i in range(n-1,-1,-1):
    idx = sub.index(ans[i])
    result-=len(sub)-idx-1
    sub.remove(sub[idx])
print(str(result)+'/'+str((n*(n-1))//2))
