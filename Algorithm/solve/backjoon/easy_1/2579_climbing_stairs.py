import sys

if __name__ == '__main__':
    stairs = int(sys.stdin.readline())

    acc_score_table = []
    score_table = [int(sys.stdin.readline()) for _ in range(stairs)]
    acc_score_table.append(score_table[0])
    if len(score_table) > 1:
        acc_score_table.append(score_table[0] + score_table[1])
    if len(score_table) > 2:
        acc_score_table.append(max(score_table[0] + score_table[2], score_table[1] + score_table[2]))

    for i in range(3, stairs):
        acc_score_table.append(max(acc_score_table[i-2] + score_table[i], acc_score_table[i-3] + score_table[i-1] + score_table[i]))

    print(acc_score_table[stairs-1])
