import sys
from collections import deque

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    my_deque = deque([i for i in range(1, n+1)])

    while my_deque:
        if len(my_deque) == 1:
            break
        my_deque.popleft()
        my_deque.append(my_deque.popleft())

    print(my_deque[0])
