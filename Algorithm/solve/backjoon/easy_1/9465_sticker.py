import sys

if __name__ == '__main__':
    test_case = int(sys.stdin.readline())
    for _ in range(test_case):
        n = int(sys.stdin.readline())
        up_sticker = list(map(int, sys.stdin.readline().replace('\n', '').split()))
        down_sticker = list(map(int, sys.stdin.readline().replace('\n', '').split()))
        up_dp_table = [up_sticker[0]]
        down_dp_table = [down_sticker[0]]

        if n >= 2:
            up_dp_table.append(down_sticker[0] + up_sticker[1])
            down_dp_table.append(down_sticker[1] + up_sticker[0])

        for i in range(2, n):
            up_dp_table.append(max(down_dp_table[i-2], down_dp_table[i-1]) + up_sticker[i])
            down_dp_table.append(max(up_dp_table[i-2], up_dp_table[i-1]) + down_sticker[i])

        print(max(max(up_dp_table), max(down_dp_table)))
