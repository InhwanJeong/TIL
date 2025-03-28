import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    input_data = [int(sys.stdin.readline()) for _ in range(n)]
    length = len(input_data)-1
    point = 20000
    count = 0
    for i in range(length, -1, -1):
        if input_data[i] >= point:
            count += input_data[i] - point + 1
            input_data[i] = point - 1
        point = input_data[i]

    print(count)
