import sys


if __name__ == '__main__':
    t = int(sys.stdin.readline())

    one_table = [0 for i in range(41)]
    one_table[1] = 1
    zero_table = [0 for i in range(41)]
    zero_table[0] = 1

    for _ in range(t):
        n = int(sys.stdin.readline())
        count_zero = 0
        count_one = 0

        if n == 0:
            count_zero += 1
        elif n == 1:
            count_one += 1
        else:
            for i in range(2, n+1):
                if one_table[i] == 0:
                    one_table[i] = one_table[i-1] + one_table[i-2]
                if zero_table[i] == 0:
                    zero_table[i] = zero_table[i-1] + zero_table[i-2]

        print(f"{zero_table[n]} {one_table[n]}")
