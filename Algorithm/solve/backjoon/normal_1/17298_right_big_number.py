import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().replace("\n", ""))

    num_list = list(map(int, sys.stdin.readline().split()))
    result = [-1 for _ in range(n)]
    stack = []

    for i in range(n-1):
        if num_list[i] < num_list[i+1]:
            result[i] = num_list[i+1]
        else:
            stack.append(i)
        while stack:
            if num_list[stack[-1]] < num_list[i + 1]:
                break
            else:
                result[stack.pop()] = num_list[i + 1]
    print(result)
"""
4
3 5 2 7

4
9 5 4 8
"""