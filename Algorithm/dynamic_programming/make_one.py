if __name__ == '__main__':
    max = 1000000
    memo = [0 for i in range(max)]

    target = int(input())

    for i in range(2, max):
        if i % 3 == 0:
            memo[i] = memo[int(i/3)] + 1
            continue

        if i % 2 == 0:
            memo[i] = memo[int(i/2)] + 1
            continue

        memo[i] = memo[i-1] + 1

    print(memo[target])


