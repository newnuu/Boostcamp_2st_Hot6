from sys import stdin
input = stdin.readline

def _15566(N : int, M : int, interest_topic : list, favor_lotus : list, log_topic : list):

    frog = {f : None for f in range(N)}
    for idx, val in enumerate(favor_lotus):
        if len(val) == 1:
            frog[idx] = 





if __name__ == "__main__":
    N, M = map(int, input().split())
    interest_topic = [list(map(int, input().split())) for _ in range(N)]
    favor_lotus = [set(map(int, input().split())) for _ in range(N)]
    log_topic = [list(map(int, input().split())) for _ in range(M)]
    _15566(N, M, interest_topic, favor_lotus, log_topic)

