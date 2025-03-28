import sys


class BackTracking():
    def __init__(self, n, m, n_list):
        self.n = n
        self.end = m
        self.n_list = n_list
        self.result_list = []
        self.process_back_tracking(str_list=[])

    def print(self):
        for item in self.result_list:
            print(item)

    def process_back_tracking(self, str_list):
        if len(str_list) == self.end:
            str_list = [str(n_list[int(i)-1]) for i in str_list]
            result = ' '.join(str_list)
            self.result_list.append(result)
            return 0

        for i in range(1, self.n+1):
            if str(i) not in str_list:
                str_list.append(str(i))
                self.process_back_tracking(str_list)
                str_list.pop()


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    n_list = sorted(list(map(int, sys.stdin.readline().replace('\n', '').split())))
    bt_program = BackTracking(n, m, n_list)
    bt_program.print()
