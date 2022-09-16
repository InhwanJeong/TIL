import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    dp_table = [1] * 90

    for i in range(2, 90):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]

    print(dp_table[n-1])
