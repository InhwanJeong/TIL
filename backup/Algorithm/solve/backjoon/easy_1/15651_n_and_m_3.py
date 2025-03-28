import sys


class BackTracking():
    def __init__(self, n, m):
        self.n = n
        self.end = m
        self.result_list = []
        self.process_back_tracking(0, str_list=[])

    def print(self):
        for item in self.result_list:
            print(item)

    def process_back_tracking(self, start, str_list):
        if start == self.end:
            result = ' '.join(str_list)
            self.result_list.append(result)
            return 0

        for i in range(1, self.n+1):
            str_list.append(str(i))
            self.process_back_tracking(start+1, str_list)
            str_list.pop()


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    bt_program = BackTracking(n, m)
    bt_program.print()
