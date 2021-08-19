from sys import stdin
input = stdin.readline

def _4150(x:int):
    fibonacci = [0, 1, 1,]
    if x == 1: return fibonacci[x]
    elif x == 2: return fibonacci[x]
    else:
        for i in range(3, x + 1):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        return fibonacci[x]

if __name__ == '__main__':
    n = int(input())
    print(_4150(n))
