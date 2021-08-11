test_num = int(input())
coordinate = [input().split() for _ in range(test_num)]
xcoordinate_dict = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8}
r_xcoordinate_dict = {v:k for k, v in xcoordinate_dict.items()}

for i in coordinate:

    # 시작점과 종료점에서 갈 수 있는 모든 좌표를 넣을 리스트 생성(시작점, 종료점 제외)
    srt_possible = []
    end_possible = []
    srt_x, srt_y = xcoordinate_dict[i[0]], int(i[1])
    end_x, end_y = xcoordinate_dict[i[2]], int(i[3])

    # 시작점과 종료점이 같은 경우
    if srt_x == end_x and srt_y == end_y:
        print(0, i[0], i[1])
        continue

    # 시작점과 종료점이 다른 경우 갈 수 있는 모든 방향에 대해 좌표 구함(시작점, 종료점 제외)
    for j in range(4):
        dx, dy = [1, 1, -1, -1,], [1, -1, 1, -1]
        srt_line_x, srt_line_y = srt_x + dx[j], srt_y + dy[j]
        end_line_x, end_line_y = end_x + dx[j], end_y + dy[j]
        
        while 1 <= srt_line_x <= 8 and 1 <= srt_line_y <= 8:
            srt_possible.append([srt_line_x, srt_line_y])
            srt_line_x += dx[j]
            srt_line_y += dy[j]

        while 1 <= end_line_x <= 8 and 1 <= end_line_y <= 8:
            end_possible.append([end_line_x, end_line_y])
            end_line_x += dx[j]
            end_line_y += dy[j]

    # 한 번에 갈 수 있는 경우
    if [end_x, end_y] in srt_possible:
        print(1, i[0], i[1], i[2], i[3])
        continue

    # 한 번에 갈 수 없느 경우
    for k in srt_possible:
        flag = False
        if k in end_possible:
            print(2, i[0], i[1], r_xcoordinate_dict[k[0]], k[1], i[2], i[3])
            flag = True
            break

    if not flag:
        print("Impossible")
