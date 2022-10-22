def fib_naive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = fib_naive(n-1) + fib_naive(n-2)
        return fib

# top-down
# recursive, stack 제한이 있음
def fib_recur_dp(n):
    pass


# bottom-up
def fib_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib_array = [0, 1]

    for i in range(2, n+1):
        num = fib_array[i-1] + fib_array[i-2]
        fib_array.append(num)
    return fib_array[n]

if __name__ == '__main__':
    # print(fib_naive(35))
    print(fib_dp(35))
