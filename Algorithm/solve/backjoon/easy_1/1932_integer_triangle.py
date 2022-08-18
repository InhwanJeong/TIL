import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    memo_table = [table[0]]

    for i in range(1, n):
        memo_table.append([])
        for j in range(i+1):
            if j == 0:
                up = memo_table[i - 1][j] + table[i][j]
                memo_table[i].append(up)
                continue
            if i == j:
                left_up = memo_table[i - 1][j - 1] + table[i][j]
                memo_table[i].append(left_up)
                continue

            up = memo_table[i - 1][j] + table[i][j]
            left_up = memo_table[i - 1][j - 1] + table[i][j]
            memo_table[i].append(max(up, left_up))

    print(max(memo_table[-1]))
