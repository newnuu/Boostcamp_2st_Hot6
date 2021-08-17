'''
https://www.acmicpc.net/problem/3077
임진왜란
[풀이]
1. 정답을 dictionary 형태로 저장
=> 이 때 key를 정답 단어로, value를 index로 저장
2. 입력받은 단어에 대해서 2개씩 뽑는 반복문
=> 먼저 뽑은 단어가 뒷 단어보다 딕셔너리 값이 작은 경우를 센다
'''
n = int(input())
answer = input().split()
dic = {val : idx for idx, val in enumerate(answer)}
result = input().split()
print([dic[result[i]] < dic[result[j]] for i in range(n) for j in range(i, n)].count(1),'/',(n*(n-1)//2),sep='')
