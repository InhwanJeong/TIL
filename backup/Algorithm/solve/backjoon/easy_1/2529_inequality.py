import sys


def get_upper_integer(flag, result):
    if len(result) == k + 1:
        print(''.join(map(str, result)))
        return 1

    for i in range(9, -1, -1):
        if flag or flag == None:
            return 1
        if visited[i]:
            continue
        if result:
            if inequality_list[len(result)-1] == '<' and result[-1] > i:
                return 0
            if inequality_list[len(result)-1] == '>' and result[-1] < i:
                return 0
        visited[i] = 1
        result.append(i)
        flag = get_upper_integer(flag, result)
        item = result.pop()
        visited[item] = 0


def get_down_integer(flag, result):
    if len(result) == k+1:
        print(''.join(map(str, result)))
        return 1

    for i in range(0, 10):
        if flag or flag == None:
            return 1
        if visited[i]:
            continue
        if result:
            if inequality_list[len(result)-1] == '<' and result[-1] > i:
                return 0
            if inequality_list[len(result)-1] == '>' and result[-1] < i:
                return 0

        visited[i] = 1
        result.append(i)
        flag = get_down_integer(flag, result)
        item = result.pop()
        visited[item] = 0


if __name__ == '__main__':
    k = int(sys.stdin.readline())
    inequality_list = sys.stdin.readline().replace('\n', '').split()
    visited = [0] * 10
    get_upper_integer(0, [])
    get_down_integer(0, [])
