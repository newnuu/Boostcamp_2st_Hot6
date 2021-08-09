import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def solution(N, G):
    viruses = [0] * (N + 1) # 각 pc들의 virus 상태
    Q = deque([1]) # 1번 pc가 virus 걸림
    viruses[1] = 1

    while Q: # BFS
        cur_pc = Q.popleft() 
        for linked_pc in G[cur_pc]: # cur_pc와 link 된 pc들 중에서,
            if viruses[linked_pc] == 0: # 처음 접근하는 pc이면,
                viruses[linked_pc] = 1 # virus pc
                Q.append(linked_pc) # linked_pc 이후도 탐색

    return sum(viruses) - 1

if __name__ == '__main__':
    N = int(input())
    E = int(input())
    G = defaultdict(list)
    for _ in range(E):
        c1, c2 = map(int, input().split())
        G[c1].append(c2)
        G[c2].append(c1)
    result = solution(N, G)
    print(result)
