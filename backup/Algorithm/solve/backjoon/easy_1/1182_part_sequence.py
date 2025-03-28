import sys


def recursion(i, sum_value):
    if i == n:
        return

    if sum_value + n_list[i] == s:
        sum_value_list.append(0)

    recursion(i + 1, sum_value)
    recursion(i + 1, sum_value + n_list[i])


if __name__ == '__main__':
    n, s = map(int, sys.stdin.readline().replace('\n', '').split())
    n_list = list(map(int, sys.stdin.readline().replace('\n', '').split()))
    sum_value_list = []

    recursion(0, 0)

    if sum_value_list:
        print(len(sum_value_list))
    else:
        print(0)

