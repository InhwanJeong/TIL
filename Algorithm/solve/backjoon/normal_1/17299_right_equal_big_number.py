import sys
from collections import Counter

if __name__ == '__main__':
    n = int(sys.stdin.readline().replace("\n", ""))

    result = [-1] * n
    num_list = list(map(int, sys.stdin.readline().split()))
    count_num_list = Counter(num_list)

    wait_stack = []

    pre_value = 0
    for i, value in enumerate(num_list):
        value = count_num_list[value]
        if i == 0:
            pre_value = value
            continue

        if pre_value < value:
            result[i - 1] = num_list[i]
            while wait_stack:
                if wait_stack[-1][0] >= value:
                    break
                _, j = wait_stack.pop()
                result[j] = num_list[i]
        else:
            wait_stack.append([pre_value, i-1])

        pre_value = value

    print(' '.join(map(str, result)))

"""
7
1 1 2 3 4 2 1
"""