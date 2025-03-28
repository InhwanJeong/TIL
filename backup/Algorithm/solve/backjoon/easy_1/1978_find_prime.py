import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    number_list = list(map(int, sys.stdin.readline().replace('\n', '').split()))
    prime_check = [0] * 1000
    prime_list = []

    for i in range(2, 1000):
        if not prime_check[i]:
            prime_list.append(i)
            for j in range(i+i, 1000, i):
                prime_check[j] = 1

    result_list = [i for i in number_list if i in prime_list]
    print(len(result_list))
