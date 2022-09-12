import sys


def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().replace('\n', '').split())

    gcd = get_gcd(a, b)
    lcm = (a*b) // gcd

    print(gcd)
    print(lcm)
