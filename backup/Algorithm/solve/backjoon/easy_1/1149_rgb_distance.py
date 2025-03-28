import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    rgb_table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    dp_table = [rgb_table[0]]
    for i in range(1, n):
        r = min(dp_table[i-1][1], dp_table[i-1][2]) + rgb_table[i][0]
        g = min(dp_table[i-1][2], dp_table[i-1][0]) + rgb_table[i][1]
        b = min(dp_table[i-1][0], dp_table[i-1][1]) + rgb_table[i][2]
        dp_table.append([r, g, b])

    print(min(dp_table[-1]))
