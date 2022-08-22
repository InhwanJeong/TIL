import sys

if __name__ == '__main__':
    a = int(sys.stdin.readline())

    progression_list = list(map(int, sys.stdin.readline().split()))
    dp_table = [1]
    for i in range(1, a):
        temp = [dp_table[j] for j in range(i) if progression_list[i] < progression_list[j]]
        if temp:
            dp_table.append(max(temp) + 1)
        else:
            dp_table.append(1)
    print(max(dp_table))
