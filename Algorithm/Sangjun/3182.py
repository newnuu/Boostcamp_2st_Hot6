from sys import stdin
input = stdin.readline

def _3182(n:int, lt:list):

    meet_num = []

    # 모든 선배로부터 시작해 본다.
    for idx, val in enumerate(lt):

        # 다음 선배로 갈 때 이미 만난 선배인지 확인하는 list
        meet = [0] * n

        # 만나지 않은 선배라면 만났다는 표시를 해준 후 다음 선배로 이동 
        while meet[idx] == 0:
            meet[idx] = 1
            idx = val - 1
            val = lt[idx]

        # 만난 선배의 수 저장
        meet_num.append(sum(meet))

    print(meet_num.index(max(meet_num)) + 1)


if __name__ == '__main__':
    n = int(input())
    reply = [int(input()) for _ in range(n)]
    _3182(n, reply)
