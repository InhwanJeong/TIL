from array import array


def solution(board, moves):
    answer = 0
    result_array = array('b', [])
    board_length = len(board)

    print(moves)
    for move in moves:
        move = move - 1  # 배열 위치와 맞춰주기 위함
        for i in range(board_length):
            if board[i][move] != 0:
                if result_array and result_array[-1] == board[i][move]:
                    result_array.pop()
                    board[i][move] = 0
                    answer += 2
                    break
                result_array.append(board[i][move])
                board[i][move] = 0
                break
    return answer
