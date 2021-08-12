# 9081번  단어 맞추기 골드 5

def func(word):
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  # replace 사용하면 다 바뀌어서 리스트에 넣음
  word = list(word)
  word_sort = word[:]
  word_sort.sort(reverse=True)

  # 큰 순서대로 정렬되어 있는 경우
  if word == word_sort:
    return word

  # 순서가 랜덤하게 있는 경우
  for i in range(1, len(word)):
    # 앞 뒤 비교해 앞이 더 작은 곳이 i
    if alphabet.index(word[-i]) > alphabet.index(word[-i - 1]):
      for j in range(1, len(word)):
        # 끝에서부터 i보다 큰 값을 찾아 j
        if alphabet.index(word[-i - 1]) < alphabet.index(word[-j]):
          # swap 파이썬에선 한 줄로 가능
          # change = word[-i]
          # word[-i] = word[-j - 1]
          # word[-j - 1] = change
          # i값과 j값을 swap
          word[-i - 1], word[-j] = word[-j], word[-i - 1]

          # 위치 바꾼 i의 뒷 부분 반대로 정렬
          word[-i:] = reversed(word[-i:])

          return word

t = int(input())

for _ in range(t):
  result = func(input())
  # *func(input()) 사용시 단어 사이에 공백 생김
  print("".join(result))
