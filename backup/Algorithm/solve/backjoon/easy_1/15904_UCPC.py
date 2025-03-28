import sys


if __name__ == '__main__':
    s = sys.stdin.readline().replace('\n', '')
    find_UCPC = list('CPCU')

    for item in s:
        if not find_UCPC:
            break
        if item == find_UCPC[-1]:
            find_UCPC.pop()

    if find_UCPC:
        print('I hate UCPC')
    else:
        print('I love UCPC')
