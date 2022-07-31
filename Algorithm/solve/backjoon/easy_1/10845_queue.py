import sys
from collections import deque

if __name__ == '__main__':
    iter_num = int(input())
    queue = deque([])

    for i in range(iter_num):
        input_data = sys.stdin.readline().replace("\n", "")
        split_input_data = input_data.split()

        if split_input_data[0] == 'size':
            print(len(queue))

        if split_input_data[0] == 'push':
            queue.append(split_input_data[1])

        if queue:
            if split_input_data[0] == 'pop':
                print(queue.popleft())

            if split_input_data[0] == 'empty':
                print(0)

            if split_input_data[0] == 'front':
                print(queue[0])

            if split_input_data[0] == 'back':
                print(queue[-1])
        else:
            if split_input_data[0] == 'empty':
                print(1)

            if split_input_data[0] == 'front' or split_input_data[0] == 'back' or split_input_data[0] == 'pop':
                print(-1)
