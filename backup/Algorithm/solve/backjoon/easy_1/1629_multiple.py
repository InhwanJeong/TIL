import sys


def recursive_process(a, b, c):
    if b == 1:
        return a % c

    value = recursive_process(a, int(b/2), c)
    value = value * value % c
    if b % 2 == 0:
        return value
    return value * a % c


if __name__ == '__main__':
    a, b, c = map(int, sys.stdin.readline().split())

    print(recursive_process(a, b, c))
