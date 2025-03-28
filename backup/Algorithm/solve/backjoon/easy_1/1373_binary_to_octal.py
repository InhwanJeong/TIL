import sys

if __name__ == '__main__':
    print(oct(int(sys.stdin.readline().replace('\n', ''), 2))[2:])
