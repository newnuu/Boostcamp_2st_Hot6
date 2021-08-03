num_words = int(input())
num_list = [input() for _ in range(num_words)]
num_list.sort(key = lambda x: len(x))
ans_list = num_list.copy()
cnt = 0
for idx, val in enumerate(num_list):
    for i in range(idx + 1, num_words):
        if val == num_list[i][:len(val)]:
            ans_list.remove(val)
            break
print(len(ans_list))
