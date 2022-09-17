import sys
from collections import deque

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace('\n', '').split())
    node_edge_list = [list() for _ in range(n)]
    all_visited = []

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().replace('\n', '').split())
        node_edge_list[b-1].append(a-1)

    for i, node_list in enumerate(node_edge_list):
        node_list = list(set(node_list))
        visited = [0] * n
        visited[i] = 1
        my_queue = deque(node_list)

        for node in node_list:
            if node == i:
                continue
            visited[node] = 1

        while my_queue:
            node = my_queue.popleft()

            for friend_node in node_edge_list[node]:
                if not visited[friend_node]:
                    visited[friend_node] = 1
                    my_queue.append(friend_node)

        all_visited.append(sum(visited))

    hacking_computer = max(all_visited)
    for i, item in enumerate(all_visited):
        if item == hacking_computer:
            print(i+1, end=' ')

"""
6 5
1 2
2 3
3 1
4 5
5 6

12 11
2 1
3 2
4 2
5 1
2 5
6 7
7 8
8 9
9 10
10 11
11 12

5 4
3 2
4 3
3 4
4 5
"""