import sys
from collections import deque

if __name__ == '__main__':
    computers = int(sys.stdin.readline().replace("\n", ""))
    network_couple_number = int(sys.stdin.readline().replace("\n", ""))

    graph = [sys.stdin.readline().replace("\n", "").split() for _ in range(network_couple_number)]
    queue = deque([])
    visited = [False for _ in range(computers)]
    count = 0

    visited[0] = True
    target = 1
    queue.extend(list(set([j for item in graph for j in item if str(target) in item and not visited[int(j)-1]])))
    for item in queue:
        visited[int(item)-1] = True

    while queue:
        target = int(queue.popleft())
        visited[target-1] = True
        queue.extend(list(set([j for item in graph for j in item if str(target) in item and not visited[int(j) - 1]])))
        for item in queue:
            visited[int(item) - 1] = True
        count += 1

    print(count)
