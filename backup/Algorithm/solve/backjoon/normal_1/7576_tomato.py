import sys
from collections import deque


def bfs(board, visited, queue):
    next_queue = deque([])

    direct_x = [-1, 1, 0, 0]  # 위, 아, 왼, 오
    direct_y = [0, 0, -1, 1]  # 위, 아, 왼, 오
    count = 0
    while True:
        while queue:
            position_x, position_y = queue.popleft()

            for k in range(4):
                temp_x = position_x + direct_x[k]
                temp_y = position_y + direct_y[k]

                if temp_y < 0 or temp_x < 0 or temp_x >= n or temp_y >= m:
                    continue

                if board[temp_x][temp_y] == 0 and not visited[temp_x][temp_y]:
                    next_queue.append([temp_x, temp_y])
                    visited[temp_x][temp_y] = True
                    board[temp_x][temp_y] = 1

        if not next_queue:
            break

        count += 1
        while next_queue:
            queue.append(next_queue.popleft())

    for i, item in enumerate(board):
        for j, value in enumerate(item):
            if value == 0:
                count = -1

    return count


if __name__ == '__main__':
    m, n = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [([0] * m) for i in range(n)]
    queue = deque([])

    for i, item in enumerate(board):
        for j, value in enumerate(item):
            if value == 1:
                queue.append([i, j])

    print(bfs(board, visited, queue))

"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""