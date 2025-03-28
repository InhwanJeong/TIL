import sys


def check_valid_ps(input_data: str):
    ps_stack = []
    check_valid = True

    for char in input_data:
        if char == "(":
            ps_stack.append(char)
        else:
            if not ps_stack:
                check_valid = False
                break
            if ps_stack[-1] == "(":
                ps_stack.pop()
            else:
                check_valid = False
                break

    if check_valid and not ps_stack:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    iter_num = int(input())

    for i in range(iter_num):
        input_data = sys.stdin.readline().replace("\n", "")

        check_valid_ps(input_data)
