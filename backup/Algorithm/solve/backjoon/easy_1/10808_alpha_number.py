import sys
import string
from collections import Counter

if __name__ == '__main__':
    s = list(sys.stdin.readline().replace("\n", ''))
    lower_alphabet_list = list(string.ascii_lowercase)
    count_list = Counter(s)

    for lower_alphabet in lower_alphabet_list:
        print(f'{count_list[lower_alphabet]}', end=" ")
