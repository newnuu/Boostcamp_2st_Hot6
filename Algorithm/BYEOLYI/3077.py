# 3077번  임진왜란  실버 3

from sys import stdin

n = int(stdin.readline())
correct_answer = list(stdin.readline().split())
student_answer = list(stdin.readline().split())
# 학생 점수, 총점
a, b = 0, n * (n - 1) // 2

for i in range(n):
  for j in range(i + 1, n):
    student1 = student_answer.index(correct_answer[i])
    student2 = student_answer.index(correct_answer[j])
    
    # 정답 순서와 같을 경우
    if student1 < student2:
      a += 1
      
print(str(a) + "/" + str(b))
