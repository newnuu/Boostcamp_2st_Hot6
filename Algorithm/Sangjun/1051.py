def _1051(n, m, num_list):
    for k in range(min(n, m), -1, -1):
        for i in range(n):
            for j in range(m):
            # for k in range(min(n, m) - 1, 0, -1):
                if (i + k < n) and (j + k < m):
                    if num_list[i][j] == num_list[i + k][j] == num_list[i][j + k] == num_list[i + k][j + k]:
                        return (k + 1) ** 2
        

n, m = map(int, input().split())
num_list = [list(map(int, list(input()))) for _ in range(n)]
ans = _1051(n, m, num_list)
print(ans)
