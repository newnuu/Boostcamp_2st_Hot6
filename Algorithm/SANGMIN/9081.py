'''
https://www.acmicpc.net/problem/9081
단어 맞추기
[풀이]
1. 각 단어가 다음 단어로 넘어가는 규칙은 다음과 같다
1-1. 마지막 단어부터 역순으로 탐색한다.
1-2. 앞 단어가 뒷 단어보다 작은 구간을 찾는다.
=> 여기서 작다는 의미는 사전순으로 앞에 온다는 의미이다
1-3. 찾았다면, 이 앞단어보다 뒤에 있는 단어들 중에 앞단어보다는 크면서 가장 최소인 단어가 이 자리로 온다.
1-4. 그리고 이 앞단어는 뒷단어들 사이에 껴서 최초 오름차순 정렬된 상태로 된다.
2. 이 규칙을 만족하지 않는 단어는 가장 마지막 단어이므로 그대로 반환한다.
'''
n = int(input())
for _ in range(n):
    word = list(input())
    for idx in range(len(word)-1, 0, -1):
        if word[idx] > word[idx-1]:
            a, b = min([(w, jdx) for jdx, w in enumerate(word[idx:]) if w > word[idx - 1]])
            print(''.join(word[:idx-1]+[a]+sorted(word[idx:idx+b]+word[idx+b+1:]+[word[idx-1]])))
            break
    else:
        print(''.join(word))
