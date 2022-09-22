import sys


class BackTracking():
    def __init__(self, n, m):
        self.n = n
        self.end = m
        self.result_list = []
        self.visited = [False] * 9
        self.count = 0
        self.process_back_tracking(1, str_list=[])

    def print(self):
        for item in self.result_list:
            print(item)

    def process_back_tracking(self, start, str_list):
        if len(str_list) == self.end:
            result = ' '.join(sorted(str_list))
            self.result_list.append(result)
            return 0

        for i in range(start, self.n+1):
            str_list.append(str(i))
            self.process_back_tracking(i, str_list)
            str_list.pop()


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    bt_program = BackTracking(n, m)
    bt_program.print()
