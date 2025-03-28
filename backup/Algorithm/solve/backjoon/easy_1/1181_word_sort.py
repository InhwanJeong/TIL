import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().replace("\n", ""))

    word_list = list(set([sys.stdin.readline().replace("\n", "") for _ in range(n)]))
    word_list.sort()
    for word in sorted(word_list, key=lambda x: len(x)):
        print(word)
