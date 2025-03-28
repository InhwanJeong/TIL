import sys


def check_color(n, table, row, column, answer):
    check_value = table[row][column]

    for i in range(n):
        for j in range(n):
            if table[i + row][j + column] != check_value:
                return False

    return True


def make_color_paper(n, table, row, column, answer):
    if check_color(n, table, row, column, answer):
        answer[table[row][column]] += 1
        return 0

    next_n = int(n/2)

    for i in range(2):
        for j in range(2):
            make_color_paper(next_n, table, row + i * next_n, column + j * next_n, answer)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    answer = [0, 0]

    make_color_paper(n, table, 0, 0, answer)
    print(answer[0])
    print(answer[1])
