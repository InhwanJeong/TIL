import sys

INF = pow(2, 31) - 1

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    meeting_list = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: x[0])
    meeting_list = sorted(meeting_list, key=lambda x: x[1])
    max_end = 0
    count = 0
    for start, end in meeting_list:
        if start >= max_end:
            count += 1
            max_end = end
    print(count)
