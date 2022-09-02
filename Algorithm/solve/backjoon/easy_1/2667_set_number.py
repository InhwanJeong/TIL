import sys
from collections import deque


def get_number(n, visited_board):
    my_queue = deque([])
    direct_x = [-1, 0, 1, 0] # 왼 위 오 아
    direct_y = [0, -1, 0, 1]

    result_list = []

    for i in range(n):
        for j in range(n):
            if visited_board[i][j] == 1:
                my_queue.append([i, j])
                visited_board[i][j] = 0
                count = 1
                while my_queue:
                    position_x, position_y = my_queue.popleft()

                    for k, x in enumerate(direct_x):
                        temp_x = position_x + x
                        temp_y = position_y + direct_y[k]

                        if temp_y < 0 or temp_x < 0 or temp_x >= n or temp_y >= n:
                            continue

                        if visited_board[temp_x][temp_y]:
                            count += 1
                            visited_board[temp_x][temp_y] = 0
                            my_queue.append([temp_x, temp_y])
                result_list.append(count)

    print(len(result_list))
    print(' '.join(map(str, sorted(result_list))))


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    visited_board = [list(map(int, sys.stdin.readline().replace('\n',''))) for _ in range(n)]
    get_number(n, visited_board)
