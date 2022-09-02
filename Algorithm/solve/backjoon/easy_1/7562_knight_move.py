import sys
from collections import deque


def move_knight(n, start, end):
    visited = [([False] * n) for i in range(n)]
    move_dp = [([0] * n) for i in range(n)]
    direct_x = [-2, -1, 2, 1, -2, -1, 2, 1]  # 왼위, 위왼, 오위, 위오, 왼아, 아왼, 오아, 아오
    direct_y = [-1, -2, -1, -2, 1, 2, 1, 2]
    my_queue = deque([start])

    while my_queue:
        position_x, position_y = my_queue.popleft()
        if position_x == end[0] and position_y == end[1]:
            break

        for i, x in enumerate(direct_x):
            temp_x = position_x + x
            temp_y = position_y + direct_y[i]

            if temp_x < 0 or temp_y < 0 or temp_y >= n or temp_x >= n:
                continue

            if not visited[temp_x][temp_y]:
                visited[temp_x][temp_y] = True
                move_dp[temp_x][temp_y] += move_dp[position_x][position_y] + 1
                my_queue.append([temp_x, temp_y])

    x, y = end
    print(move_dp[x][y])


if __name__ == '__main__':
    test_case = int(sys.stdin.readline())

    for _ in range(test_case):
        n = int(sys.stdin.readline())
        start = list(map(int, sys.stdin.readline().split()))
        end = list(map(int, sys.stdin.readline().split()))

        move_knight(n, start, end)
