import sys
from collections import deque

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace("\n", "").split())
    maze = [list(map(int, list(sys.stdin.readline().replace("\n", "")))) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    distance = [[1 for _ in range(m)] for _ in range(n)]
    queue = deque([])

    position_x = 0
    position_y = 0
    direct_x = [-1, 1, 0, 0]  # 위, 아, 왼, 오
    direct_y = [0, 0, -1, 1]  # 위, 아, 왼, 오
    visited[0][0] = True

    while True:
        if [n-1, m-1] in queue:
            break

        if queue:
            position_x, position_y = queue.popleft()

        for i in range(4):
            temp_x = position_x + direct_x[i]
            temp_y = position_y + direct_y[i]

            if temp_y < 0 or temp_x < 0 or temp_x >= n or temp_y >= m:
                continue

            if maze[temp_x][temp_y] == 1 and not visited[temp_x][temp_y]:
                queue.append([temp_x, temp_y])
                distance[temp_x][temp_y] += distance[position_x][position_y]
                visited[temp_x][temp_y] = True

    # for i in maze:
    #     print(i)
    # for i in visited:
    #     print(i)
    # for i in distance:
    #     print(i)
    print(distance[n-1][m-1])
