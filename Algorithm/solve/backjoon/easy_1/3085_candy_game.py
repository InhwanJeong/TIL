import sys

if __name__ == '__main__':
    n = int(input())

    board = []
    for i in range(n):
        input_data = sys.stdin.readline().replace("\n", "")
        board.append([i for i in input_data])

    max_value = 1

    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if (i-1) >= 0: # 위
                count = 0
                board[i - 1][j], board[i][j] = board[i][j], board[i - 1][j]

                # while :
                #     if

                board[i - 1][j], board[i][j] = board[i][j], board[i - 1][j]
            if (j-1) >= 0: # 왼쪽
                print(board[i][j-1], i, j)
            if (i+1) < len(board): # 아래
                print(board[i+1][j], i, j)
            if (j+1) < len(board): # 오른쪽
                print(board[i][j+1], i, j)

    print(max_value)
