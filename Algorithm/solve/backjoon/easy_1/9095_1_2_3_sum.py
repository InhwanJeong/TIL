import sys

if __name__ == '__main__':
    test_case = int(sys.stdin.readline())

    n_list = [int(sys.stdin.readline()) for _ in range(test_case)]
    dp_table = [1, 2, 4]

    iter_num = max(n_list)
    for i in range(3, iter_num):
        dp_table.append(dp_table[i-3] + dp_table[i-2] + dp_table[i-1])

    for i in n_list:
        print(dp_table[i-1])
