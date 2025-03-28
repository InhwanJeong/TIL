import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    n_list = [sys.stdin.readline().replace('\n', '') for _ in range(n)]

    length = len(n_list[0])

    for i in range(length):
        char_list = [item[i] for item in n_list]
        value = char_list[0]
        char_list = [item for item in char_list if item != value]
        print('?', end='') if len(char_list) > 0 else print(value, end='')
