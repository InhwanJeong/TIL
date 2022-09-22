import sys
import itertools
import copy


def up_angle_cctv(pos_i, pos_j, new_board):
    while pos_i > 0:
        pos_i -= 1
        if new_board[pos_i][pos_j] == 6:
            break
        if new_board[pos_i][pos_j] == 0:
            new_board[pos_i][pos_j] = 5
    return new_board


def down_angle_cctv(pos_i, pos_j, new_board):
    while pos_i < n - 1:
        pos_i += 1
        if new_board[pos_i][pos_j] == 6:
            break
        if new_board[pos_i][pos_j] == 0:
            new_board[pos_i][pos_j] = 5
    return new_board


def left_angle_cctv(pos_i, pos_j, new_board):
    while pos_j > 0:
        pos_j -= 1
        if new_board[pos_i][pos_j] == 6:
            break
        if new_board[pos_i][pos_j] == 0:
            new_board[pos_i][pos_j] = 5
    return new_board


def right_angle_cctv(pos_i, pos_j, new_board):
    while pos_j < m - 1:
        pos_j += 1
        if new_board[pos_i][pos_j] == 6:
            break
        if new_board[pos_i][pos_j] == 0:
            new_board[pos_i][pos_j] = 5
    return new_board


def set_four_angle_cctv_in_board():
    four_angle_cctv = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 5:
                four_angle_cctv.append([i, j])

    new_board = copy.deepcopy(board)
    for i, j in four_angle_cctv:
        new_board = left_angle_cctv(i, j, new_board)
        new_board = right_angle_cctv(i, j, new_board)
        new_board = up_angle_cctv(i, j, new_board)
        new_board = down_angle_cctv(i, j, new_board)

    return new_board


def get_cctv():
    temp_list = []

    for i in range(n):
        for j in range(m):
            if 0 < board[i][j] < 5:
                temp_list.append([board[i][j], i, j])

    return sorted(temp_list, key=lambda x: x[0], reverse=True)


def get_min_count():
    new_board = copy.deepcopy(board)
    cctv_type_process = {
        1: {
            0: lambda x, y, z: up_angle_cctv(x, y, z),
            1: lambda x, y, z: down_angle_cctv(x, y, z),
            2: lambda x, y, z: left_angle_cctv(x, y, z),
            3: lambda x, y, z: right_angle_cctv(x, y, z)
        },
        2: {
            0: lambda x, y, z: up_angle_cctv(x, y, down_angle_cctv(x, y, z)),
            1: lambda x, y, z: right_angle_cctv(x, y, left_angle_cctv(x, y, z))
        },
        3: {
            0: lambda x, y, z: up_angle_cctv(x, y, right_angle_cctv(x, y, z)),
            1: lambda x, y, z: down_angle_cctv(x, y, left_angle_cctv(x, y, z)),
            2: lambda x, y, z: left_angle_cctv(x, y, up_angle_cctv(x, y, z)),
            3: lambda x, y, z: right_angle_cctv(x, y, down_angle_cctv(x, y, z))
        },
        4: {
            0: lambda x, y, z: up_angle_cctv(x, y, right_angle_cctv(x, y, left_angle_cctv(x, y, z))),
            1: lambda x, y, z: down_angle_cctv(x, y, left_angle_cctv(x, y, right_angle_cctv(x, y, z))),
            2: lambda x, y, z: left_angle_cctv(x, y, up_angle_cctv(x, y, down_angle_cctv(x, y, z))),
            3: lambda x, y, z: right_angle_cctv(x, y, down_angle_cctv(x, y, up_angle_cctv(x, y, z)))
        }
    }
    for i, item in enumerate(cctv_list):
        cctv_type, pos_x, pos_y = item
        new_board = cctv_type_process[cctv_type][case[i]](pos_x, pos_y, new_board)

    return count_zero(new_board)


def count_zero(new_board):
    count = 0
    for i in range(n):
        for j in range(m):
            if new_board[i][j] == 0:
                count += 1
    return count


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace('\n', '').split())
    board = [list(map(int, sys.stdin.readline().replace('\n', '').split())) for _ in range(n)]
    board = set_four_angle_cctv_in_board()
    min_count = n * m

    cctv_list = get_cctv()
    combination_cctv = [[0, 1, 2, 3] if item[0] != 2 else [0, 1] for item in cctv_list]
    all_case = list(itertools.product(*combination_cctv))

    for case in all_case:
        min_count = min(get_min_count(), min_count)

    print(min_count)
