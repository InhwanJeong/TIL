import sys


class Trie:
    def __init__(self):
        self.root = {}

    def show(self):
        print(self.root)

    def insert(self, string):
        current = self.root
        for char in string:
            if char not in current:
                current[char] = {}
            current = current[char]

    def start_width(self, string):
        current = self.root
        for char in string:
            if char in current:
                current = current[char]
        return current


if __name__ == '__main__':
    test_case = int(sys.stdin.readline())

    for _ in range(test_case):
        n = int(sys.stdin.readline())
        phone_list = [sys.stdin.readline().replace('\n', '') for _ in range(n)]
        trie = Trie()
        result = False

        for string in phone_list:
            trie.insert(string + "*")

        for string in phone_list:
            search = trie.start_width(string)
            if len(search) > 1:
                result = True
                break

        if result:
            print("NO")
        else:
            print("YES")
