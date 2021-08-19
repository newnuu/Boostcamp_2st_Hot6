from sys import stdin
input = stdin.readline

# num 까지인 fibonacci수열 만든 후, 큰 수 부터 빼가면서 0 이 될 때 까지 반복.
def _9009(num : int):
    fibonacci = [0, 1]
    idx = 2
    next_num = 1
    while next_num < num:
        next_num = fibonacci[idx - 1] + fibonacci[idx - 2]
        fibonacci.append(next_num)
        idx += 1
    
    fibonacci.reverse()
    answer = []
    for i in fibonacci:
        if num - i < 0:
            continue
        elif num == 0:
            break
        else:
            num -= i
            answer.append(i)

    return reversed(answer)

if __name__ == '__main__':
    test_case = int(input())
    target_num = [int(input()) for _ in range(test_case)]
    for i in target_num:
        print(*_9009(i))


