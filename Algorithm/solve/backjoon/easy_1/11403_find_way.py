import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    board = [list(map(int, sys.stdin.readline().replace('\n', '').split()))for _ in range(n)]
    # visited = [[0 for _ in range(n)] for _ in range(n)]
    visited = []
    new_board = [list() for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                new_board[i].append(j)

    for i in range(n):
        new_visited = [0] * n
        my_stack = []
        for item in new_board[i]:
            my_stack.append(item)
            new_visited[item] = 1

        while my_stack:
            node = my_stack.pop()

            for item in new_board[node]:
                if not new_visited[item]:
                    new_visited[item] = 1
                    my_stack.append(item)

        visited.append(new_visited)

    for items in visited:
        print(' '.join(map(str, items)))
