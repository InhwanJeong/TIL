import sys


def my_combinations(result):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    start = n_list.index(result[-1]) + 1 if result else 0
    for i in range(start, n):
        if not visited[i] and (i == 0 or n_list[i] != n_list[i-1] or visited[i-1]):
            visited[i] = 1
            result.append(n_list[i])
            my_combinations(result)
            visited[i] = 0
            result.pop()


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    n_list = sorted(list(map(int, sys.stdin.readline().replace('\n', '').split())))
    visited = [0] * n

    my_combinations([])
