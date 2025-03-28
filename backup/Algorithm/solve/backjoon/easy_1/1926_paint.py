import sys
from collections import deque

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [([0] * m) for i in range(n)]
    max_dp = [1]
    queue = deque([])

    direct_x = [-1, 1, 0, 0]  # 위, 아, 왼, 오
    direct_y = [0, 0, -1, 1]  # 위, 아, 왼, 오
    count = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j] or board[i][j] == 0:
                continue

            queue.append([i, j])

            max_value = 1
            count += 1
            while queue:
                position_x, position_y = queue.popleft()

                for k in range(4):
                    temp_x = position_x + direct_x[k]
                    temp_y = position_y + direct_y[k]

                    if temp_y < 0 or temp_x < 0 or temp_x >= n or temp_y >= m:
                        continue

                    if board[temp_x][temp_y] == 1 and not visited[temp_x][temp_y]:
                        queue.append([temp_x, temp_y])
                        max_dp.append(max_value)
                        visited[temp_x][temp_y] = True
                        max_value += 1

    print(count)
    if count:
        print(max(max_dp))
    else:
        print(0)
