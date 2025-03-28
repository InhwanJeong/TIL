import sys

if __name__ == '__main__':
    iter_num = int(input())

    for i in range(iter_num):
        input_data = sys.stdin.readline().replace("\n", "")
        split_word = input_data.split()

        for word in split_word:
            print(word[::-1], end=' ')
