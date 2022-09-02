import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    coin_list = [int(sys.stdin.readline()) for _ in range(n)]

    all_use_count = 0
    while k != 0:
        n -= 1
        if n < 0:
            break

        if coin_list[n] <= k:
            count = int(k / coin_list[n])
            k %= coin_list[n]
            all_use_count += count

    print(all_use_count)
