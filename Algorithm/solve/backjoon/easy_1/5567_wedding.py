import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    node_list = [list() for _ in range(n)]
    visited = [0] * n

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().replace('\n', '').split())
        node_list[i-1].append(j-1)
        node_list[j-1].append(i-1)

    my_stack = []
    visited[0] = 1
    for node in node_list[0]:
        my_stack.append(node)
        visited[node] = 1

    while my_stack:
        new_node_list = my_stack.pop()
        for node in node_list[new_node_list]:
            visited[node] = 1

    print(visited.count(1)-1)
