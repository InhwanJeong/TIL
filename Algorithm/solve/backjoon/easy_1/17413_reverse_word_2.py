if __name__ == '__main__':
    s = input()

    reverse_stack = []
    not_change = False

    for char in s:
        if char == "<":
            while reverse_stack:
                print(reverse_stack.pop(), end="")
            not_change = True
        if not_change:
            if char == ">":
                not_change = False
            print(char, end="")
            continue
        if char == " ":
            while reverse_stack:
                print(reverse_stack.pop(), end="")
            print(" ", end="")
        else:
            reverse_stack.append(char)

    while reverse_stack:
        print(reverse_stack.pop(), end="")
