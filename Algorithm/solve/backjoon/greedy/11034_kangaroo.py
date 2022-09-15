import sys

if __name__ == '__main__':
    while True:
        try:
            a, b, c = map(int, sys.stdin.readline().replace('\n', '').split())
            count = 0
            while c-b != 1 or b-a != 1:
                count += 1
                if c-b > b-a:
                    a = b
                    b = b+1
                else:
                    c = b
                    b = b - 1
            print(count)
        except:
            break
