"""
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

입력
첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

출력
첫째 줄에 자연수 N의 최댓값을 출력한다

1 - 1
2 - 1
3 - 2
4 - 2
5 - 2
6 - 3
200 - 19

"""
import sys

if __name__ == '__main__':
    s = int(sys.stdin.readline())

    sum = 0
    pointer = 0

    while sum < s:
        pointer += 1
        sum += pointer

    if s < sum:
        print(pointer-1)
    else:
        print(pointer)

