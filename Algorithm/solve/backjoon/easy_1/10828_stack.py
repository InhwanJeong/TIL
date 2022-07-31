"""
정수를 저장하는 스택을 구현
다섯 가지 명령 처리
    push X: 정수 X를 스택에 넣는 연산이다.
    pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 스택에 들어있는 정수의 개수를 출력한다.
    empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

input
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.
문제에 나와있지 않은 명령이 주어지는 경우는 없다.

print
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
"""

import sys
import array


def stack_process(integer_stack: array, input_data: str):
    split_string = input_data.split()
    if split_string[0] == "push":
        integer_stack.append(int(split_string[1]))

    if split_string[0] == "top":
        if integer_stack:
            print(integer_stack[-1])
        else:
            print(-1)

    if split_string[0] == "pop":
        if integer_stack:
            print(integer_stack.pop())
        else:
            print(-1)

    if split_string[0] == "size":
        print(len(integer_stack))

    if split_string[0] == "empty":
        if integer_stack:
            print(0)
        else:
            print(1)

    return integer_stack


if __name__ == '__main__':
    iter_num = int(input())

    integer_stack = array.array('i', [])
    for i in range(iter_num):
        input_data = sys.stdin.readline().replace("\n", "")

        integer_stack = stack_process(integer_stack, input_data)
