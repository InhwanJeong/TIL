import sys
from collections import deque


def get_min_button_click():
    while my_queue:
        position = my_queue.popleft()
        if position == goal:
            return visited[goal] - 1

        for move in move_list:
            next_position = position + move

            if next_position < 1 or floor < next_position:
                continue

            if not visited[next_position]:
                visited[next_position] = visited[position] + 1
                my_queue.append(next_position)

    return "use the stairs"


if __name__ == '__main__':
    floor, start, goal, up, down = map(int, sys.stdin.readline().replace('\n', '').split())
    visited = [0] * (floor + 1)
    move_list = [up, -down]

    my_queue = deque([start])
    visited[start] = 1

    print(get_min_button_click())


"""
10 1 10 2 1
100 2 1 1 0
1000000 1 1000000 3 2
2 1 2 1 1
1 1 1 1 1
"""