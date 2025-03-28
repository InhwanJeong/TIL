import sys


def my_product(result):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(n):
        if i == 0 or n_list[i] != n_list[i-1] or visited[i-1]:
            visited[i] = 1
            result.append(n_list[i])
            my_product(result)
            visited[i] = 0
            result.pop()


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    n_list = sorted(list(map(int, sys.stdin.readline().replace('\n', '').split())))
    visited = [0] * n

    my_product([])
