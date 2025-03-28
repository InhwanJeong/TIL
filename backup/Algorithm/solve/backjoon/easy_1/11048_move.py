import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    maze = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    for i in range(1, n):
        maze[i][0] += maze[i-1][0]

    for i in range(1, m):
        maze[0][i] += maze[0][i-1]

    for i in range(1, n):
        for j in range(1, m):
            maze[i][j] += max(maze[i-1][j], maze[i][j-1], maze[i-1][j-1])

    print(maze[n-1][m-1])
