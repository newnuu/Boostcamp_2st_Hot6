from sys import stdin
input = stdin.readline

'''
def _1003(x:int):
    if x == 0:
        return [1, 0]
    elif x == 1:
        return [0, 1]
    else:
        return [_1003(x - 1)[0] + _1003(x - 2)[0], _1003(x - 1)[1] + _1003(x - 2)[1]]
'''


def _1003(x:int):
    fibonacci_list = [(1, 0), (0, 1)]
    for i in range(2, x + 1):
        fibonacci_list.append((fibonacci_list[i - 1][0] + fibonacci_list[i - 2][0], fibonacci_list[i - 1][1] + fibonacci_list[i - 2][1]))
    return (fibonacci_list[x][0], fibonacci_list[x][1])


if __name__ == '__main__':
    test_num = int(input())
    test_list = [int(input()) for _ in range(test_num)]
    for i in test_list:
        zero, one = _1003(i)
        print(zero, one)
