import sys
from collections import deque

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    node_edge_list = [list() for _ in range(n)]
    all_visited = []

    while True:
        i, j = map(int, sys.stdin.readline().replace('\n', '').split())

        if i == -1 and j == -1:
            break

        node_edge_list[i-1].append(j-1)
        node_edge_list[j-1].append(i-1)

    for i, node_list in enumerate(node_edge_list):
        visited = [0] * n
        my_queue = deque([])

        for node in node_list:
            my_queue.append(node)
            visited[node] = 1

        while my_queue:
            node = my_queue.popleft()

            for friend_node in node_edge_list[node]:
                if not visited[friend_node]:
                    visited[friend_node] = visited[node] + 1
                    my_queue.append(friend_node)
        all_visited.append(visited)

    for i in range(n):
        all_visited[i][i] = 0
    point_list = [max(item) for item in all_visited]
    candidate_value = min(point_list)
    candidate_list = [item for item in point_list if item == candidate_value]

    print(f'{candidate_value} {len(candidate_list)}')
    for i, point in enumerate(point_list):
        if point == candidate_value:
            print(f'{i+1}', end=' ')
