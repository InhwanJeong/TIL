import sys
from collections import deque

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    my_deque = deque([])
    input_process = {
        'size': lambda int_value: len(my_deque),
        'front': lambda int_value: my_deque[0] if my_deque else -1,
        'back': lambda int_value: my_deque[-1] if my_deque else -1,
        'empty': lambda int_value: 0 if my_deque else 1,
        'pop_front': lambda int_value: my_deque.popleft() if my_deque else -1,
        'pop_back': lambda int_value: my_deque.pop() if my_deque else -1,
        'push_front': lambda int_value: my_deque.appendleft(int_value),
        'push_back': lambda int_value: my_deque.append(int_value),
    }

    for _ in range(n):
        input_data = sys.stdin.readline().replace("/n", "").split()
        if len(input_data) == 1:
            print(input_process[input_data[0]](0))
            continue
        input_process[input_data[0]](input_data[-1])

