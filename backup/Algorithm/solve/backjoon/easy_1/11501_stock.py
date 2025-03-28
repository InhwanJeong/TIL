import sys

if __name__ == '__main__':
    test_case = int(sys.stdin.readline())

    for _ in range(test_case):
        n = int(sys.stdin.readline())
        result = 0
        stock_list = list(map(int, sys.stdin.readline().replace('\n', '').split()))
        max_value = 0

        for i in range(len(stock_list)-1, -1, -1):
            if stock_list[i] > max_value:
                max_value = stock_list[i]
            else:
                result += max_value - stock_list[i]

        print(result)
