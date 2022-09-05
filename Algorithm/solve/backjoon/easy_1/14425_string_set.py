import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace('\n', '').split())

    s = [sys.stdin.readline().replace('\n', '') for _ in range(n)]
    input_list = [sys.stdin.readline().replace('\n', '') for _ in range(m)]
    input_list = [item for item in input_list if item in s]
    print(len(input_list))
