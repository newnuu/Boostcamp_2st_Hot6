n = int(input())
words=[]
for _ in range(n):
    words.append(input())
words.sort(key = lambda x : len(x))
answer=[words[-1]]
for i in range(len(words)):
    for j in range(i+1,len(words)):
        if words[i] == words[j][:len(words[i])]:
            break
        if j==len(words)-1:
            answer.append(words[i])
print(len(answer))
