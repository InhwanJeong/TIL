import sys

if __name__ == '__main__':
    iter_num = int(input())

    wanted_stack = [int(sys.stdin.readline().replace("\n", "")) for _ in range(iter_num)]

    wanted_pointer = 0
    check_pointer = 1
    check_stack = []
    print_stack = []

    while True:
        if check_stack:
            if check_stack[-1] == wanted_stack[wanted_pointer]:
                check_stack.pop()
                print_stack.append('-')
                wanted_pointer += 1
                continue

        if check_pointer < iter_num+1:
            check_stack.append(check_pointer)
            print_stack.append('+')
            check_pointer += 1
        else:
            break

    if check_stack:
        print('NO')
    else:
        for item in print_stack:
            print(item)
