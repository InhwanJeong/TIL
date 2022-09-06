import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace('\n', '').split())
    save_dict = {}
    for _ in range(n):
       input_data = sys.stdin.readline().replace('\n', '').split()
       save_dict[input_data[0]] = input_data[1]

    for _ in range(m):
        input_data = sys.stdin.readline().replace('\n', '')
        print(save_dict[input_data])
