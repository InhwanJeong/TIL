import sys

if __name__ == '__main__':
    while True:
        string = list(sys.stdin.readline().replace('\n', ''))
        result = [0, 0, 0, 0]
        if not string:
            break
        for char in string:
            if char == ' ':
                result[-1] += 1
                continue

            if char.isdigit():
                result[-2] += 1
                continue

            if ord(char) < 97:
                result[-3] += 1
            else:
                result[-4] += 1

        print(' '.join(map(str, result)))
