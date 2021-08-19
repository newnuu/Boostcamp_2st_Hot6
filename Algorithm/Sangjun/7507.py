from sys import stdin
input = stdin.readline

# 날짜, 끝나는 시간이 빠른 순으로 경기 정렬 후,
# 현재 경기가 끝나는 시간 뒤에 시작되면서 가장빨리 끝나는 경기들을 세면 됨.
def _7507():
    
    game_num = int(input())
    game_info = sorted([list(map(int, input().split())) for _ in range(game_num)], key = lambda x: (x[0], x[2]))
    day, t, ans = 0, 0, 0
    
    # 모든 경기에 대해서 한번씩 탐색
    for game in game_info:
        
        # 날짜가 바뀌면 기준시간 초기화, 날짜 업데이트
        if day < game[0]:
            t = 0
            day = game[0]

        # 현재 경기의 종료시간 보다 시작시간이 늦는 경기중, 가장 빨리 끝나는 경기를 찾고, 기준시간 업데이트
        if t <= game[1]:
            ans += 1
            t = game[2]

    return ans


if __name__ == '__main__':
    ans = []
    test_num = int(input())
    
    for i in range(test_num):
        ans.append(_7507())
    
    for i in range(test_num):
        print(f'Scenario #{i + 1}:')
        print(ans[i])
        print()
