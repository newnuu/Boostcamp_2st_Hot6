def swap(i,j,flag):
    # 뒤에서 부터 비교할 단어 (word[i]) 와 그 이후 단어 리스트 l 
    if word[i]<l[j]: # word[i]가 l[j] 보다 작은 경우 두 문자의 자리 바꿈
        ans = word[:i]+[l[j]]+sorted([word[i]]+l[:j]+l[j+1:])
        print(''.join(ans))
        flag = 1 # flag 값으로 결과 완료 표시
        return  (i,flag)
      
    elif len(l)>j+1: # 비교할 수가 남아있으면 그 다음으로 큰 문자와 비교
        return swap(i,j+1,0)
      
    else: # 비교할 문자들이 모두 word[i]보다 앞순서이면 하나 앞문자와 비교한다
        i-=1
        return (i,0)
        
n = int(input())
for _ in range(n):
    word = list(input())
    
    # 사전상 가장 마지막 순서인 경우 단어 그대로 출력
    if word == sorted(word,reverse=True): 
        print(''.join(word))
        continue
        
    i = -2 # 뒤에서 두번째
    j = 0
    while True:
        flag = 0
        l = sorted(word[i+1:]) # 비교할 단어 사전순 정렬 ( 뒤에서부터 두개, 3개, ....)
        i,flag = swap(i,j,0) # i, j swap 0은 flag
        
        if flag ==1: # 원하는 결과 출력 시 break
            break
