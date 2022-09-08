import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    n_list = list(map(int, sys.stdin.readline().replace('\n', '').split()))
    m = int(sys.stdin.readline())
    m_list = list(map(int, sys.stdin.readline().replace('\n', '').split()))

    n_list.sort()

    for item in m_list:
        check = 0
        start, end = 0, n - 1
        while start <= end:
            middle = int((start + end)/2)
            if item == n_list[middle]:
                check = 1
                break
            elif item > n_list[middle]:
                start = middle + 1
            else:
                end = middle - 1

        print(check)


"""
5
4 1 5 2 3
5
1 3 7 9 5
"""