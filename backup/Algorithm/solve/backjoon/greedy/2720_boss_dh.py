import sys

if __name__ == '__main__':
    test_case = int(sys.stdin.readline())
    coin_list = [25, 10, 5, 1]

    for _ in range(test_case):
        change = int(sys.stdin.readline())

        for coin in coin_list:
            print(change // coin, end=' ')
            change = change % coin
        print()
