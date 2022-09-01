import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().replace("\n", ""))

    result = [-1] * n
    num_list = list(map(int, sys.stdin.readline().split()))
    wait_stack = []

    pre_value = 0
    for i, value in enumerate(num_list):
        if i == 0:
            pre_value = value
            wait_stack.append([value, i])
            continue

        if pre_value < value:
           result[i - 1] = value
        else:
            wait_stack.append([pre_value, i-1])

        while wait_stack:
            if wait_stack[-1][0] >= value:
                break
            _, i = wait_stack.pop()
            result[i] = value

        pre_value = value

    print(' '.join(map(str, result)))
