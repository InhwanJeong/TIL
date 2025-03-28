import sys

if __name__ == '__main__':
    first_string = sys.stdin.readline()
    second_string = sys.stdin.readline()

    first_length = len(first_string) + 1
    second_length = len(second_string) + 1
    dp_table = [[0] * second_length for _ in range(first_length)]

    for i in range(1, first_length-1):
        for j in range(1, second_length-1):
            if first_string[i] == second_string[j]:
                dp_table[i][j] = dp_table[i-1][j-1] + 1

    print(max([max(items) for items in dp_table]))
