import sys

if __name__ == '__main__':
    a_phone = sys.stdin.readline().replace('\n', '')
    b_phone = sys.stdin.readline().replace('\n', '')

    a_length = len(a_phone) - 1
    my_a_list = list(map(int, a_phone))
    my_b_list = list(map(int, b_phone))

    while len(my_a_list) > 1:
        temp_a_list = []
        temp_b_list = []
        for j in range(len(my_b_list)):
            if j == len(my_b_list) - 1 and len(my_a_list) == len(my_b_list):
                temp_a_list.append((my_a_list[j] + my_b_list[j]) % 10)
            else:
                temp_a_list.append((my_a_list[j] + my_b_list[j]) % 10)
                temp_b_list.append((my_a_list[j+1] + my_b_list[j]) % 10)

        my_a_list = temp_a_list
        my_b_list = temp_b_list

    print(f'{my_a_list[-1]}{my_b_list[-1]}')
