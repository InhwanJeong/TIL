import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in range(1, n+1):
        print(f"{'*' * i}{' ' * ((n-i) * 2)}{ '*' * i}")

    for i in range(n-1, -1, -1):
        print(f"{'*' * i}{' ' * ((n-i) * 2)}{ '*' * i}")
