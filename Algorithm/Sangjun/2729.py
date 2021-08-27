from sys import stdin
input = stdin.readline

# 이진수 변환함수로 구현
def _2729(bin_list : list):
    for i in bin_list:
        a = int(i[0], 2)
        b = int(i[1], 2)
        c = str(bin(a + b))[2:]
        print(c)

if __name__ == "__main__":
    test_num = int(input())
    bin_list = [input().split() for _ in range(test_num)]
    _2729(bin_list)
