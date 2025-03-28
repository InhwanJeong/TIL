import sys


def get_max_earnings(location, items):
    if location >= n:
        return 0

    for i in range(location, n):
        if i + counseling_list[i][0] <= n:
            items.append(counseling_list[i][1])
            result.append(sum(items))
            get_max_earnings(i + counseling_list[i][0], items)
            items.pop()


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    counseling_list = [list(map(int, sys.stdin.readline().replace('\n', '').split())) for _ in range(n)]
    result = [0]
    get_max_earnings(0, [])
    print(max(result))
