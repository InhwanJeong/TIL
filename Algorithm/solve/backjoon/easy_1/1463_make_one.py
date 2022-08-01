import sys

if __name__ == '__main__':
    integer_n = int(sys.stdin.readline().replace("\n", ""))

    table = [0 for i in range(1000001)]

    for i in range(2, integer_n+1):
        temp = []
        if i % 3 == 0:
            temp.append(table[int(i/3)] + 1)

        if i % 2 == 0:
            temp.append(table[int(i/2)] + 1)

        table[i] = table[i-1] + 1
        table[i] = min(temp)

    print(table[integer_n])
