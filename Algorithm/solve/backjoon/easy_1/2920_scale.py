import sys

if __name__ == '__main__':
    scale = list(map(int, sys.stdin.readline().replace('\n', '').split()))
    ascending = [i for i in range(1, 9)]
    descending = [i for i in range(8, 0, -1)]
    if scale == ascending:
        print('ascending')
    elif scale == descending:
        print('descending')
    else:
        print('mixed')
