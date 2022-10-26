if __name__ == '__main__':
    max = 1000000+1
    memo = [0 for i in range(max)]

    target = int(input())


    for i in range(2, target+1):
        temp = []
        if i % 3 == 0:
            temp.append(memo[int(i/3)] + 1)

        if i % 2 == 0:
            temp.append(memo[int(i/2)] + 1)

        temp.append(memo[i-1] + 1)
        print(temp)
        memo[i] = min(temp)

    print(memo[target])


