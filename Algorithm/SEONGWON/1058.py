import sys
input = sys.stdin.readline

def solution(N, arr):
    answer = 0
    friends = [set() for _ in range(N)] # 친구는 중복되지 않으므로 set을 사용

    def dfs(target, person, depth): # DFS (친구를 찾으려는 person, 현재 탐색할 person, 관계 depth)
        if depth == 3: # 깊이가 3인 친구는 2-friend가 아니다
            return

        for friend in range(N): # 현재 person의 친구 탐색
            if target != friend and arr[person][friend] == 'Y':
                friends[target].add(friend)
                dfs(target, friend, depth + 1) 

    for t in range(N): # 모든 사람들에 대해 친구 탐색
        dfs(t, t, 1)

    return max([len(f) for f in friends]) # 가장 많은 친구 수

if __name__ == '__main__':
    N = int(input())
    arr = [input().strip() for _ in range(N)]
    result = solution(N, arr)
    print(result)
