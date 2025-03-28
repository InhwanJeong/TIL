import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    dp_table = [[0] * 10 for _ in range(n+1)]
    for i in range(1, 10):
        dp_table[1][i] = 1

    for i in range(2, n+1):
        for j in range(10):
            if j == 0:
                dp_table[i][j] = dp_table[i-1][1]
            elif j == 9:
                dp_table[i][j] = dp_table[i-1][8]
            else:
                dp_table[i][j] = dp_table[i-1][j-1] + dp_table[i-1][j+1]

    print(sum(dp_table[n]) % 1000000000)
