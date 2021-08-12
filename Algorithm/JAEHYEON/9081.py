import sys
input = sys.stdin.readline

'''
next_permutation 함수
예시 : 136541
1. 끝에서 부터 비교하여 앞에 것이 더 작은 곳을 i 라고 한다.
        i
    1   3   6   5   4   1
2. 끝에서 부터 i값보다 큰 값을 찾아 j로 정한다.
                    j
    1   3   6   5   4   1
3. i 값과 j값을 서로 바꾼다.
        i           j
    1   4   6   5   3   1
4. i 뒤에 있는 것들을 순서를 뒤집어 준다.
        i           j
    1   4   1   3   5   6
'''

def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i+1]: # i값 찾기
        i -= 1
    if i == -1: # i 가 -1이 되면 주어진 단어가 마지막
        return False
    
    j = len(arr) - 1 
    while arr[i] >= arr[j]: # j값 찾기
        j -= 1

    arr[i], arr[j] = arr[j], arr[i] # i값과 j값 서로 바꾸기
    result = arr[:i+1]
    result.extend(list(reversed(arr[i+1:]))) # i뒤에 있는 것들 순서 뒤집기
    return result

T = int(input())
while T:
    temp = list(input().rstrip())
    answer = next_permutation(temp)
    if not answer: # 단어가 마지막 단어라면
        print("".join(temp)) # 주어진 단어 출력
    else: # 아니라면
        print("".join(answer)) # next permutation값 출력
    T -= 1
