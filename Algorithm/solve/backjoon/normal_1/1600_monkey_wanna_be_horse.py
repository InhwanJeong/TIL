import sys
from collections import deque
import pprint


def get_min_move():
    monkey_direct_x = [-1, 0, 1, 0]
    monkey_direct_y = [0, -1, 0, 1]
    horse_direct_x = [-1, -2, -1, 2, 1, -2, 1, 2]
    horse_direct_y = [-2, -1, 2, -1, -2, 1, 2, 1]

    my_queue = deque([[0, 0, 1, 0]])
    visited[0][0][0] = 1

    while my_queue:
        position_x, position_y, min_count, k_count = my_queue.popleft()

        if k_count < k:
            for j, _ in enumerate(horse_direct_x):
                temp_x = position_x + horse_direct_x[j]
                temp_y = position_y + horse_direct_y[j]

                if temp_x < 0 or temp_y < 0 or temp_x >= height or temp_y >= width:
                    continue

                if not visited[temp_x][temp_y][k_count+1] and board[temp_x][temp_y] != 1:
                    visited[temp_x][temp_y][k_count+1] = min_count
                    my_queue.append([temp_x, temp_y, min_count+1, k_count+1])

        for j, _ in enumerate(monkey_direct_x):
            temp_x = position_x + monkey_direct_x[j]
            temp_y = position_y + monkey_direct_y[j]

            if temp_x < 0 or temp_y < 0 or temp_x >= height or temp_y >= width:
                continue

            if not visited[temp_x][temp_y][k_count] and board[temp_x][temp_y] != 1:
                visited[temp_x][temp_y][k_count] = min_count
                my_queue.append([temp_x, temp_y, min_count+1, k_count])


if __name__ == '__main__':
    k = int(sys.stdin.readline())
    width, height = map(int, sys.stdin.readline().replace('\n', '').split())
    board = [list(map(int, sys.stdin.readline().replace('\n', '').split())) for _ in range(height)]
    visited = [[[0] * (k+1) for _ in range(width)] for _ in range(height)]
    get_min_move()
    pprint.pprint(visited)
    if width == height == 1:
        print(0)
    elif max(visited[height-1][width-1]) == 0:
        print(-1)
    else:
        temp = [item for item in visited[height-1][width-1] if item > 0]
        print(min(temp))

