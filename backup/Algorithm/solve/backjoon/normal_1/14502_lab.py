import sys
from collections import deque
from itertools import combinations
import copy

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace("\n", "").split())
    original_graph = [list(map(int, sys.stdin.readline().replace("\n", "").split())) for _ in range(n)]

    extra_wall = 3
    direct_x = [-1, 1, 0, 0]  # 위, 아, 왼, 오
    direct_y = [0, 0, -1, 1]  # 위, 아, 왼, 오

    combinations_items = list(combinations([[i, j] for i, items in enumerate(original_graph) for j, item in enumerate(items) if item == 0], extra_wall))

    area_list = []
    for items in combinations_items:
        area = 0
        graph = copy.deepcopy(original_graph)
        for item in items:
            x, y = item
            graph[x][y] = 1

        virus_queue = deque([[i, j] for i, items in enumerate(graph) for j, item in enumerate(items) if item == 2])
        while virus_queue:
            queue = deque([virus_queue.popleft()])
            while queue:
                position_x, position_y = queue.popleft()
                for i in range(4):
                    temp_x = position_x + direct_x[i]
                    temp_y = position_y + direct_y[i]

                    if temp_y < 0 or temp_x < 0 or temp_x >= n or temp_y >= m:
                        continue

                    if graph[temp_x][temp_y] == 0:
                        graph[temp_x][temp_y] = 2
                        queue.append([temp_x, temp_y])

        for i in graph:
            area += i.count(0)

        area_list.append(area)

    print(max(area_list))
