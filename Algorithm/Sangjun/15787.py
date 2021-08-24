from sys import stdin
input = stdin.readline


def _15787(N : int, command : list):
    train = [[0] * 20 for _ in range(N)]
    for cmd in command:

        # 1번 명령 : 사람 없을 때만 고려
        if cmd[0] == 1:
            if not train[cmd[1] - 1][cmd[2] - 1]:
                train[cmd[1] - 1][cmd[2] - 1] = 1
        
        # 2번 명령 : 사람 있을 때만 고려
        elif cmd[0] == 2:
            if train[cmd[1] - 1][cmd[2] - 1]:
                train[cmd[1] - 1][cmd[2] - 1] = 0
        
        # 3번 명령 : 마지막 사람 자르고 앞에 안탔다는 표시
        elif cmd[0] == 3:
            train[cmd[1] - 1] = [0] + train[cmd[1] - 1][:-1]
        
        # 4번 명령 : 앞사람 자르고 마지막에 안탔다는 표시
        elif cmd[0] == 4:
            train[cmd[1] - 1] = train[cmd[1] - 1][1:] + [0]
    
    
    # 배열같은 기차 제거
    pass_train = []
    for i in train:
        if i not in pass_train:
            pass_train.append(i)

    print(len(pass_train))


if __name__ == '__main__':
    N, M = map(int, input().split())
    command = [list(map(int, input().split())) for _ in range(M)]
    _15787(N, command)
