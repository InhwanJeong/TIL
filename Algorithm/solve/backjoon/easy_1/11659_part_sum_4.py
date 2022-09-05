import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace('\n', '').split())
    board = list(map(int, sys.stdin.readline().replace('\n', '').split()))
    dp_table = [0]*n
    dp_table[0] = board[0]

    for i in range(1, n):
        dp_table[i] = dp_table[i-1] + board[i]

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().replace('\n', '').split())
        if i > 1:
            print(dp_table[j - 1]-dp_table[i-2])
        else:
            print(dp_table[j - 1])
