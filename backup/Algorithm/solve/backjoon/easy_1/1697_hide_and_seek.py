import sys
from collections import deque


def bfs(n, k):
    count = 0
    queue = deque([n])
    next_queue = deque([])
    visited = [0] * 200000

    while n != k:
        if k in queue:
            break
        count += 1
        while queue:
            value = queue.popleft()
            if value - 1 >= 0 and not visited[value - 1]:
                visited[value-1] = 1
                next_queue.append(value - 1)

            if value + 1 < 100001 and not visited[value + 1]:
                visited[value + 1] = 1
                next_queue.append(value + 1)

            if value * 2 < 200000 and not visited[value * 2]:
                visited[value * 2] = 1
                next_queue.append(value * 2)

        while next_queue:
            queue.append(next_queue.popleft())

    return count


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())

    print(bfs(n, k))
