import sys
from collections import deque


def get_minute():
    # print(board)
    # print(visited)
    # print(end)
    direct_f = [0, 0, 0, 0, 1, -1]
    direct_r = [-1, 0, 1, 0, 0, 0] # 왼 위 오 아 윗 아래
    direct_c = [0, -1, 0, 1, 0, 0]

    while my_queue:
        position_f, position_r, position_c = my_queue.popleft()
        if position_f == end[0] and position_r == end[1] and position_c == end[2]:
            return visited[end[0]][end[1]][end[2]]

        for index, f in enumerate(direct_f):
            temp_position_f = position_f + f
            temp_position_r = position_r + direct_r[index]
            temp_position_c = position_c + direct_c[index]

            if temp_position_f < 0 or temp_position_r < 0 or temp_position_c < 0 or \
                    temp_position_f >= floor or temp_position_r >= row or temp_position_c >= column:
                continue

            if not visited[temp_position_f][temp_position_r][temp_position_c] and (board[temp_position_f][temp_position_r][temp_position_c] == '.'
                                                                                   or board[temp_position_f][temp_position_r][temp_position_c] == 'E'):
                visited[temp_position_f][temp_position_r][temp_position_c] = visited[position_f][position_r][position_c] + 1
                my_queue.append([temp_position_f, temp_position_r, temp_position_c])

    return "Trapped!"


if __name__ == '__main__':
    while True:
        floor, row, column = map(int, sys.stdin.readline().replace('\n', '').split())
        if not floor and not row and not column:
            break

        board = []
        visited = [[[0 for _ in range(column)] for _ in range(row)] for _ in range(floor)]
        end = []
        my_queue = deque([])

        for i in range(floor):
            temp_board = [list(sys.stdin.readline().replace('\n', '')) for _ in range(row)]
            board.append(temp_board)
            sys.stdin.readline().replace('\n', '')
            for j, items in enumerate(temp_board):
                for k, item in enumerate(items):
                    if item == "S":
                        visited[i][j][k] = 1
                        my_queue.append([i, j, k])
                    if item == "E":
                        end = [i, j, k]

        result = get_minute()
        if type(result) == int:
            print(f'Escaped in {result-1} minute(s).')
        else:
            print(result)
