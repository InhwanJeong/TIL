import sys

if __name__ == '__main__':
    k = int(sys.stdin.readline())

    stack = []
    for _ in range(k):
        num = int(sys.stdin.readline())
        if num != 0:
            stack.append(num)
        else:
            if stack:
                stack.pop()

    if stack:
        print(sum(stack))
    else:
        print(0)
