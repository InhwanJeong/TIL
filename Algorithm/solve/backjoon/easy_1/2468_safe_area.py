import sys
from collections import deque


def get_area(n, visited_board):
    my_queue = deque([])
    direct_x = [-1 ,0, 1, 0] # 왼 위 오 아
    direct_y = [0, -1, 0, 1]

    result_list = []

    for i in range(n):
        for j in range(n):
            if visited_board[i][j] == 0:
                my_queue.append([i, j])
                visited_board[i][j] = 1
                count = 1
                while my_queue:
                    position_x, position_y = my_queue.popleft()

                    for k, x in enumerate(direct_x):
                        temp_x = position_x + x
                        temp_y = position_y + direct_y[k]

                        if temp_y < 0 or temp_x < 0 or temp_x >= n or temp_y >= n:
                            continue

                        if not visited_board[temp_x][temp_y]:
                            count += 1
                            visited_board[temp_x][temp_y] = 1
                            my_queue.append([temp_x, temp_y])
                result_list.append(count)

    return len(result_list)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    safe_area = 0
    iter_value = max(map(max, board))
    for i in range(1, iter_value):
        visited_board = [[1 if i >= k else 0 for k in j] for j in board ]
        safe_area = max(safe_area, get_area(n, visited_board))

    print(safe_area if safe_area else 1)
