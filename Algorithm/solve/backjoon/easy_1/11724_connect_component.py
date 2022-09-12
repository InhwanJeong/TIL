import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace('\n', '').split())
    line_stack = [list(map(int, sys.stdin.readline().replace('\n', '').split())) for _ in range(m)]
    node_list = [list() for _ in range(n)]
    visited = [0] * n

    for i, j in line_stack:
        node_list[i-1].append(j-1)
        node_list[j-1].append(i-1)

    count = 0
    for i, items in enumerate(node_list):
        if visited[i]:
            continue
        count += 1
        my_stack = []
        for item in items:
            my_stack.append(item)
            visited[item] = 1
        while my_stack:
            node = my_stack.pop()

            for j in node_list[node]:
                if not visited[j]:
                    my_stack.append(j)
                    visited[j] = 1

    print(count)
