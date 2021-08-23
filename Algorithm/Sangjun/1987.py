from sys import stdin
input = stdin.readline

def _1987(x : int, y : int, alpha : str):
    global result
    cnt = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # BFS 탐색하면서 중복되는 알파벳인지 확인하기
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in alpha:
            # 새로 방문 했다면 알파벳 추가
            _1987(nx, ny, alpha + board[nx][ny])
        else:
            cnt += 1
    # 가장 많이 갔을 때를 답으로
    if cnt == 4:
        result = max(result, len(alpha))
        return

if __name__ == '__main__':
    R, C = map(int, input().split())
    board = [list(input()) for _ in range(R)]
    result = 0
    _1987(0, 0, board[0][0])
    print(result)
