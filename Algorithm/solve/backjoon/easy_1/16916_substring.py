import sys
import re

if __name__ == '__main__':
    s = sys.stdin.readline().replace('\n', '')
    p = sys.stdin.readline().replace('\n', '')

    if re.search(p, s):
        print(1)
    else:
        print(0)

