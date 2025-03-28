import sys
from collections import deque


def get_length(n):
    result = 0
    count = 1
    temp = 1

    while n > 10:
        if n < 9 * temp:
            break
        result += 9 * count * temp
        n -= 9 * temp
        count += 1
        temp *= 10

    return result + n * count


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().replace('\n', '').split())
    count = 1
    temp = 1

    if get_length(n) < k:
        print(-1)
    else:
        while True:
            if k < 9 * temp * count:
                break
            k -= 9 * temp * count
            count += 1
            temp *= 10

        mod = k % count
        k = int((k-count) / count)
        temp += k

        my_queue = deque(list(str(temp)))
        my_queue.appendleft(my_queue.pop())
        print(int(my_queue[mod]))
