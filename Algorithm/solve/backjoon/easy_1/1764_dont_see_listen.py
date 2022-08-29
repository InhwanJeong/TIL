import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    listen_list = [sys.stdin.readline().replace("\n", "") for _ in range(n)]
    see_list = [sys.stdin.readline().replace("\n", "") for _ in range(m)]

    listen_see_list = sorted(list(set(listen_list) & set(see_list)))

    print(len(listen_see_list))
    for item in listen_see_list:
        print(item)


