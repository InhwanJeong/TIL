import sys
from collections import deque

if __name__ == '__main__':
    test_case = int(sys.stdin.readline().replace("\n", ""))

    for i in range(test_case):
        row, col, iter_num = map(int, sys.stdin.readline().replace("\n", "").split())

        worm_count = 0
        graph = [list(map(int, sys.stdin.readline().replace("\n", "").split())) for _ in range(iter_num)]
        visited = [False for _ in range(iter_num)]

        for j in range(iter_num):
            if visited[j]:
                continue
            worm_count += 1
            queue = deque([j])
            visited[0] = True

            while queue:
                target = queue.popleft()
                up = [graph[target][0], graph[target][1] - 1]
                down = [graph[target][0], graph[target][1] + 1]
                left = [graph[target][0] - 1, graph[target][1]]
                right = [graph[target][0] + 1, graph[target][1]]

                if up in graph:
                    target = graph.index(up)
                    if not visited[target]:
                        queue.append(target)
                        visited[target] = True

                if down in graph:
                    target = graph.index(down)
                    if not visited[target]:
                        queue.append(target)
                        visited[target] = True

                if left in graph:
                    target = graph.index(left)
                    if not visited[target]:
                        queue.append(target)
                        visited[target] = True

                if right in graph:
                    target = graph.index(right)
                    if not visited[target]:
                        queue.append(target)
                        visited[target] = True

        print(worm_count)
