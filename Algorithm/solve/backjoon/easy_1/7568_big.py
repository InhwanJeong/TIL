import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    x_y_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

    for i, item in enumerate(x_y_list):
        count = 1
        for j, item in enumerate(x_y_list):
            if x_y_list[i][0] < x_y_list[j][0] and x_y_list[i][1] < x_y_list[j][1]:
                count += 1
        print(count, end=" ")
