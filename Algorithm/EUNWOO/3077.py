n = int(input())
ans = input().split()
sub = input().split()
result=(n*(n-1))//2
for i in range(n-1,-1,-1): # 정답 리스트의 가장 마지막 인덱스부터
    idx = sub.index(ans[i])
    result-=len(sub)-idx-1 # 가장 마지막 인덱스부터 하므로 그 순서 뒤에는 원래 아무것도 없어야하므로 그 순서보다 뒤에 있는 단어 개수(잘못된 순서) 전체에서 빼기
    sub.remove(sub[idx]) # 완료 후 현재 가장 뒷순서인 단어를 리스트에서 제거
print(str(result)+'/'+str((n*(n-1))//2))
