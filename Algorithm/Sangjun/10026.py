from collections import deque
num = int(input())
painting = [' '.join(input()).split() for _ in range(num)]

# 적녹색약 구분하기 위한 새로운 리스트 생성
painting2 = []
for i in painting:
    temp_lt = []
    for j in i:
        if j == 'G':
            temp_lt.append('R')
        else:
            temp_lt.append(j)
    painting2.append(temp_lt)


# BFS로 그림을 탐색하면서 무슨 색으로 시작하는지의 개수만 세면 된다.
def _10026(num, painting):

    queue = deque()
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    visit = [[0] * num for _ in range(num)]
    RGB = {'R' : 0, 'G' : 0, 'B' : 0}
    
    # RGB 각각의 색에 대하여 그래프를 세 번 돈다.
    for i in 'RGB':
        for j in range(num):
            for k in range(num):
                
                # 확인하고자 하는 색과 탐색하고 있는 그래프의 색이 같고, 방문x
                if painting[j][k] == i and not visit[j][k]:
                    visit[j][k] = 1
                    RGB[i] += 1
                    queue.append((j, k))

                    while queue:
                        x, y = queue.popleft()
                        
                        for l in range(4):
                            nx, ny = x + dx[l], y + dy[l]
                            
                            # 그림 범위 안에서, 방문하지 않았고, 주변의 색이 현재 탐색하고 있는 색과 같다면 
                            if 0 <= nx < num and 0 <= ny < num and not visit[nx][ny] and painting[nx][ny] == i:
                                visit[nx][ny] = 1
                                queue.append((nx, ny))
    
    return sum(RGB.values())

  
  
print(_10026(num, painting), _10026(num, painting2))
