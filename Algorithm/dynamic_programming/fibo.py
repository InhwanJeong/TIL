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

# bottom-up
def fib_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib_array = [0, 1]


if __name__ == '__main__':
    print(fib_naive(35))
