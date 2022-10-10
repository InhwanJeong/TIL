import sys
from array import array

if __name__ == '__main__':
    tops_array_length = int(sys.stdin.readline())
    tops = list(map(int, sys.stdin.readline().split()))
    result_value = []
    result_index = []
    stand_by_value = []
    stand_by_index = []

    while tops:
        position = tops.index(tops[-1])
        pop_item = tops.pop()

        if tops and tops[-1] > pop_item:
            result_value.append(position)
            result_index.append(position)
        else:
            stand_by_value.append(pop_item)
            stand_by_index.append(position)

        while tops and stand_by_value and min(stand_by_value) < tops[-1]:
            index = stand_by_value.index(min(stand_by_value))
            result_index.append(stand_by_index[index])
            result_value.append(position)

            stand_by_value.remove(min(stand_by_value))
            stand_by_index.remove(stand_by_index[index])

    for i in range(tops_array_length):
        if i in result_index:
            print(result_value[result_index.index(i)], end=' ')
        else:
            print(0, end=' ')
