import sys


def hanoi_process(stack, start, goal, n):
    if n == 0:
        return 0

    hanoi_process(stack, start, 6-start-goal, n-1)
    stack.append([start, goal])
    hanoi_process(stack, 6-start-goal, goal, n-1)

    return stack


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    stack = hanoi_process([], 1, 3, n)

    print(len(stack))
    for item in stack:
        print(f'{item[0]} {item[1]}')
