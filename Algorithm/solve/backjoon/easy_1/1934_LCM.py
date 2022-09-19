import sys


def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


if __name__ == '__main__':
    test_case = int(sys.stdin.readline())
    for _ in range(test_case):
        a, b = map(int, sys.stdin.readline().replace('\n', '').split())

        gcd = get_gcd(a, b)
        lcm = (a*b) // gcd
            
        print(lcm)
