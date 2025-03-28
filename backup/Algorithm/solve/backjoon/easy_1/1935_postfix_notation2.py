import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    notations = list(sys.stdin.readline().replace('\n', ''))
    data_list = [int(sys.stdin.readline()) for _ in range(n)]
    stack = []
    result = 0
    operate_process = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    for notation in notations:
        if notation in ['+', '-', '/', '*']:
            value_2 = stack.pop()
            value_1 = stack.pop()
            result = operate_process[notation](value_1, value_2)
            stack.append(result)
            continue
        stack.append(data_list[ord(notation) - 65])

    print(f'{result:.2f}')
