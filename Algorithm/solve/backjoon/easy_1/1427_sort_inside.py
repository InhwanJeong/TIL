import sys

if __name__ == '__main__':
    n = sorted(list(sys.stdin.readline().replace('\n', '')), reverse=True)
    print(''.join(n))
