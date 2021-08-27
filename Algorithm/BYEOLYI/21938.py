# 21938번 | 영상처리 | 실버 2

# 최대 재귀 깊이를 늘림
import sys
sys.setrecursionlimit(10 ** 6)

# 세로 길이가 n이고 가로 길이가 m인 화면
n, m = map(int, input().split())
# rgb 평균, 새로운 화면, 기존 화면
new, new_screen, screen = [], [], [list(map(int, input().split())) for _ in range(n)]
# 경계값 t
t = int(input())

# 모든 픽셀에서 세 가지 색상을 평균내어 경계값(t)보다 크거나 같으면 픽셀의 값을 255로, 작으면 0으로 바꿔서 새로운 화면으로 저장
for i in range(n):
  for j in range(m * 3):
    if j + 2 <= m * 3 and j % 3 == 0:
      mean = screen[i][j] + screen[i][j + 1] + screen[i][j + 2]

      if int(mean / 3) >= t:
        new.append(255)
      else:
        new.append(0)

  new_screen.append(new)
  new = []

def dfs(x, y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  # 화면에 물체가 있는 경우
  if new_screen[x][y] == 255:
    new_screen[x][y] = 1
    # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

result = 0

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)
