import sys

if __name__ == '__main__':
    s = sys.stdin.readline().replace("\n", '').split()
    print(int(s[0] + s[1]) + int(s[2] + s[3]))
