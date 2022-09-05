import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    result = 0
    count = 1
    temp = 1

    while n > 10:
        if n < 9 * temp:
            break
        result += 9 * count * temp
        n -= 9 * temp
        count += 1
        temp *= 10

    print(result + n*count)
