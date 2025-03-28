import sys

if __name__ == '__main__':
    init_string = sys.stdin.readline().replace("\n", "")
    iter_num = int(sys.stdin.readline().replace("\n", ""))

    cursor = len(init_string)
    left_stack = [char for char in init_string]
    right_stack = []

    for i in range(iter_num):
        input_data = sys.stdin.readline().replace("\n", "")

        if input_data[0] == 'L' and left_stack:
            right_stack.append(left_stack.pop())

        if input_data[0] == 'D'and right_stack:
            left_stack.append(right_stack.pop())

        if input_data[0] == "P":
            left_stack.append(input_data[2])

        if input_data[0] == "B" and left_stack:
            left_stack.pop()

    for item in left_stack:
        print(item, end='')

    while right_stack:
        print(right_stack.pop(), end='')
