import sys

if __name__ == '__main__':
    input_data = sys.stdin.readline().replace("\n", "")
    stack = []
    result = 0
    for i, bracket in enumerate(input_data):
        if bracket == "(":
            stack.append(bracket)
            continue

        if stack and bracket == ")":
            stack.pop()
            if input_data[i-1] == ")":
                result += 1

            if len(stack) > 0 and input_data[i-1] == "(":
                result += len(stack)

    print(result)
