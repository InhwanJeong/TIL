import sys
from collections import deque

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace('\n','').split())
    node_edge_list = [list() for _ in range(n)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().replace('\n', '').split())
        node_edge_list[a-1].append(b-1)
        node_edge_list[b-1].append(a-1)

    my_queue = deque(node_edge_list[0])
    visited = [0] * n
    visited[0] = 1
    for node in node_edge_list[0]:
        visited[node] = 2

    while my_queue:
        node = my_queue.popleft()

        for friend_node in node_edge_list[node]:
            if not visited[friend_node]:
                my_queue.append(friend_node)
                visited[friend_node] = visited[node] + 1

    distance = max(visited) - 1
    num = len([node for node in visited if node == distance+1])
    print(f'{visited.index(distance+1)+1} {distance} {num}')
