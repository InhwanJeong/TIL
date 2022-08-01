import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().replace("\n", ""))

    memo_table = [0, 1, 2]

    for i in range(3, n+1):
        memo_table.append((memo_table[i-1] + memo_table[i-2]) % 10007)

    print(memo_table[n])
