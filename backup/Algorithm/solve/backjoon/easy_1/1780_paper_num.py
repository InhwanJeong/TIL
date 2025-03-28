import sys


def check_paper(n, table, row, column):
    check_value = table[row][column]
    for i in range(n):
        for j in range(n):
            if table[row + i][column + j] != check_value:
                return False

    return True


def recursive_process(n, table, row, column, answer):
    if check_paper(n, table, row, column):
        answer[table[row][column]] += 1
        return 0

    next_n = int(n/3)

    for i in range(3):
        for j in range(3):
            recursive_process(int(n/3), table, row + i * next_n, column + j * next_n, answer)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    answer = [0, 0, 0]
    recursive_process(n, table, 0, 0, answer)
    print(answer[-1])
    print(answer[-3])
    print(answer[-2])
