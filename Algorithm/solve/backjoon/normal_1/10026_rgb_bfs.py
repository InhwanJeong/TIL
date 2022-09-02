import sys
from collections import deque


def get_area(n, board, rg_state):
    my_queue = deque([])
    direct_x = [-1, 0, 1, 0] # 왼 위 오 아
    direct_y = [0, -1, 0, 1]
    visited = [[0] * n for _ in range(n)]

    result_list = []

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                if rg_state and not board[i][j] == 'B':
                    board[i][j] = 'G'
                my_queue.append([i, j])
                visited[i][j] = 1
                count = 1
                while my_queue:
                    position_x, position_y = my_queue.popleft()

                    for k, x in enumerate(direct_x):
                        temp_x = position_x + x
                        temp_y = position_y + direct_y[k]

                        if temp_y < 0 or temp_x < 0 or temp_x >= n or temp_y >= n:
                            continue

                        if rg_state and not board[temp_x][temp_y] == 'B':
                            board[temp_x][temp_y] = 'G'

                        if not visited[temp_x][temp_y] and board[position_x][position_y] == board[temp_x][temp_y]:
                            count += 1
                            visited[temp_x][temp_y] = 1
                            my_queue.append([temp_x, temp_y])
                result_list.append(count)
    print(len(result_list), end=' ')


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    board = [list(sys.stdin.readline().replace('\n', '')) for _ in range(n)]
    get_area(n, board, 0)
    get_area(n, board, 1)
