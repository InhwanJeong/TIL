import sys
from collections import deque

if __name__ == '__main__':
    n, k = sys.stdin.readline().replace("\n", "").split()
    n = int(n)
    k = int(k)

    circle_table = deque([i+1 for i in range(n)])
    result_list = []
    while circle_table:
        for i in range(k-1):
            circle_table.append(circle_table.popleft())
        result_list.append(circle_table.popleft())

    print(f'<{", ".join(map(str, result_list))}>')
