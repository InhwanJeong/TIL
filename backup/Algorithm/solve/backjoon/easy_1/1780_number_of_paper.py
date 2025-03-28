import sys


def process_paper(n, n_table, start, end):
    if n == 1:
        # print(n_table[stxart][end])
        return 0

    for i in range(start*3, (start+1)*3):
        for j in range(end*3, (end+1)*3):
            print(i, j, " - ", n_table[start][end])

    next_n = int(n/3)
    for i in range(9):
        process_paper(next_n, n_table, int(i/3) * next_n, (i % 3) * next_n)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    n_table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    process_paper(n, n_table, 0, 0)

"""
3
1 1 1
0 0 0
1 1 -1

9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
"""