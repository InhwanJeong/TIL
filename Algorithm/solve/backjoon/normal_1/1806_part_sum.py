import sys

if __name__ == '__main__':
    n, s = map(int, sys.stdin.readline().replace("\n", "").split())

    iter_list = list(map(int, sys.stdin.readline().replace("\n", "").split()))

    left_pointer = 0
    right_pointer = 0
    part_sum = iter_list[left_pointer]
    min_len = n

    while left_pointer <= right_pointer and left_pointer < n -1:
        if part_sum < s:
            if right_pointer < n - 1:
                right_pointer += 1
                part_sum += iter_list[right_pointer]
            else:
                if left_pointer < n - 1:
                    left_pointer += 1
                    part_sum -= iter_list[left_pointer]

        if part_sum >= s:
            min_len = min(min_len, right_pointer - left_pointer + 1)
            if left_pointer < n - 1:
                part_sum -= iter_list[left_pointer]
                left_pointer += 1
            if part_sum >= s:
                min_len = min(min_len, right_pointer - left_pointer + 1)

    if min_len < n:
        print(min_len)
    else:
        print(0)
