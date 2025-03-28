import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    milk_list = list(map(int, sys.stdin.readline().replace('\n', '').split()))

    eat_state = 0
    count = 0

    for milk in milk_list:
        if milk == eat_state:
            count += 1
            eat_state = (eat_state + 1) % 3

    print(count)
