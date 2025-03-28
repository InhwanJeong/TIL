import sys
import math

if __name__ == '__main__':
    r = int(sys.stdin.readline())

    print(f'{math.pi * pow(r, 2):.6f}')
    print(f'{2 * pow(r, 2):.6f}')
