import sys


def z_process(n, position_r, position_c):
    if n == 0:
        return 0

    half = pow(2, n-1)

    if position_r < half and position_c < half:
        return z_process(n - 1, position_r, position_c)
    if position_r < half <= position_c:
        return half * half + z_process(n - 1, position_r, position_c - half)
    if position_r >= half > position_c:
        return 2 * half * half + z_process(n - 1, position_r - half, position_c)
    return 3 * half * half + z_process(n-1, position_r-half, position_c-half)


if __name__ == '__main__':
    n, r, c = map(int, sys.stdin.readline().split())

    print(z_process(n, r, c))
