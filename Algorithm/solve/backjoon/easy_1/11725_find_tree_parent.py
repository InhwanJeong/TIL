import sys
from collections import deque

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    graph = [list() for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(n-1):
        parent_node, son_node = map(int, sys.stdin.readline().replace('\n', '').split())
        graph[parent_node].append(son_node)
        graph[son_node].append(parent_node)

    start = 1
    visited[start] = 1
    my_queue = deque([1])

    while my_queue:
        parent_node = my_queue.popleft()
        for item in graph[parent_node]:
            if not visited[item]:
                visited[item] = parent_node
                my_queue.append(item)

    for i in visited[2:]:
        print(i)

