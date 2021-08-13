from sys import stdin
testnum = int(stdin.readline())
word_list = [list(stdin.readline().strip()) for _ in range(testnum)]

def _9081(word):
    for i in range(len(word) - 1, 0, -1):
        if word[i-1] < word[i]:
            temp = i-1
            for j in range(len(word) - 1, 0, -1):
                if word[j] > word[temp]:
                    word[temp], word[j] = word[j], word[temp]
                    word = word[:temp + 1] + sorted(word[temp + 1:])
                    return print(''.join(word))
    return print(''.join(word))


if __name__ == "__main__":
    for word in word_list:
        _9081(word)
