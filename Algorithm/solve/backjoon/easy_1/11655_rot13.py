import sys
import string

if __name__ == '__main__':
    s = list(sys.stdin.readline().replace('\n', ''))
    lower_list = list(string.ascii_lowercase)
    upper_list = list(string.ascii_uppercase)

    for char in s:
        if char in lower_list:
            print(lower_list[(lower_list.index(char) + 13) % 26], end='')
            continue
        if char in upper_list:
            print(upper_list[(upper_list.index(char) + 13) % 26], end='')
            continue
        print(char, end='')
