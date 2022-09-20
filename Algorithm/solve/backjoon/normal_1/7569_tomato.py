import sys
from pprint import pprint
from collections import deque


def get_ripe_tomato():
    ripe_tomato_list = []
    for i, floor in enumerate(board):
        for j, items in enumerate(floor):
            for k, item in enumerate(items):
                if item == 1:
                    visited[i][j][k] = 1
                    ripe_tomato_list.append([i, j, k])
                if item == -1:
                    visited[i][j][k] = 1

    return ripe_tomato_list


def get_ripe_day():
    direct_x = [-1, 0, 1, 0, 0, 0]
    direct_y = [0, -1, 0, 1, 0, 0]
    direct_z = [0, 0, 0, 0, 1, -1]
    my_queue = deque(get_ripe_tomato())

    while my_queue:
        position_x, position_y, position_z = my_queue.popleft()

        for i, _ in enumerate(direct_x):
            temp_x = position_x + direct_x[i]
            temp_y = position_y + direct_y[i]
            temp_z = position_z + direct_z[i]

            if temp_x < 0 or temp_y < 0 or temp_z < 0 or temp_x >= h or temp_y >= n or temp_z >= m:
                continue

            if not visited[temp_x][temp_y][temp_z] and board[temp_x][temp_y][temp_z] == 0:
                visited[temp_x][temp_y][temp_z] = visited[position_x][position_y][position_z] + 1
                my_queue.append([temp_x, temp_y, temp_z])

    visited_check = [item for floor in visited for items in floor for item in items if item == 0]
    max_check = [item for floor in visited for items in floor for item in items]
    if visited_check:
        print(-1)
    else:
        print(max(max_check)-1)


if __name__ == '__main__':
    m, n, h = map(int, sys.stdin.readline().replace('\n', '').split())
    board = [[list(map(int, sys.stdin.readline().replace('\n', '').split())) for _ in range(n)] for _ in range(h)]
    ripe_check = [item for floor in board for items in floor for item in items if item == 0]

    if ripe_check:
        visited = [[[0] * m for _ in range(n)] for _ in range(h)]
        get_ripe_day()
    else:
        print(0)
