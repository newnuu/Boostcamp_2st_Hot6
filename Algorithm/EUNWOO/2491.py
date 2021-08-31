n = int(input())
s = list(map(int,input().split()))

if s==sorted(s) or s==sorted(s,reverse=True): # 완전히 정렬된 수열일 경우 전체 길이 return
    print(n)
    exit()
    
ans=[]
start = 0 # 오름차순
desc =0 # 내림차순
for i in range(n-1):
    # 오름차순 확인
    if s[i]>s[i+1]: # 다음 수가 더 큰 경우 
        ans.append(i-start+1) #지금까지의 길이 저장
        start = i+1 # 시작 기준 변경
    # 내림차순 확인    
    if s[i]<s[i+1]:
        ans.append(i-desc+1) #지금까지의 길이 저장
        desc = i+1 # 시작 기준 변경
ans.append(n-start) # 마지막 길이 
ans.append(n-desc) # 마지막 길이
print(max(ans)) # 최대값 출력
