import sys

if __name__ == '__main__':
    input_data = list(sys.stdin.readline().replace('\n', ''))
    length = len(input_data)
    check = input_data[0]
    result = 1

    for i in range(1, length):
        if check == input_data[i]:
            continue
        check = input_data[i]
        result += 1
    if result:
        print(int(result/2))
    else:
        print(0)
