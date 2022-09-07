import sys


class Trie:
    def __init__(self):
        self.root = {}
        self.locked_file = {}

    def show(self):
        print(self.root)
        print(self.locked_file)

    def insert(self, string):
        current_node = self.root
        for char in string:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]

    def lock_file(self, string):
        current_node = self.locked_file
        for char in string:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]

    def delete_all(self, delete_list):
        min_value = 0
        for item in delete_list:
            if self.__search(item):
                min_value += 1
        print(min_value)

    def __search(self, string):
        current_node = self.root
        for char in string:
            if char in current_node:
                current_node = current_node[char]
            else:
                return 0
        self.__delete(string)
        return 1

    def __delete(self, string):
        file_current_value = self.root
        lock_current_value = self.locked_file
        for i, char in enumerate(string):
            if char in lock_current_value:
                lock_current_value = lock_current_value[char]
            else:
                if i == 0:
                    for j, key in enumerate(file_current_value.keys()):
                        if key in list(lock_current_value.keys()):
                            break
                        if len(file_current_value.keys())-1 == j:
                            self.root = {}
                del file_current_value[char]
                break
            file_current_value = file_current_value[char]


if __name__ == '__main__':
    test_case = int(sys.stdin.readline())

    for _ in range(test_case):
        trie = Trie()
        n = int(sys.stdin.readline())
        delete_list = []
        for _ in range(n):
            input_data = sys.stdin.readline().replace('\n', '')
            delete_list.append(input_data)
            trie.insert(input_data + '*')

        m = int(sys.stdin.readline())
        for _ in range(m):
            input_data = sys.stdin.readline().replace('\n', '')
            trie.lock_file(input_data + '*')
        trie.delete_all(delete_list)
