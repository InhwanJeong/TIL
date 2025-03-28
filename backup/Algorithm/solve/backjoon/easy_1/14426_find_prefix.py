import sys


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, string):
        current_node = self.root
        for char in string:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]

    def search(self, string):
        current_node = self.root
        for char in string:
            if char not in current_node:
                return False
            current_node = current_node[char]
        return True


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace('\n', '').split())

    trie = Trie()
    count = 0

    for _ in range(n):
        input_data = sys.stdin.readline().replace('\n', '')
        trie.insert(input_data + "*")

    for _ in range(m):
        input_data = sys.stdin.readline().replace('\n', '')
        result = trie.search(input_data)
        if result:
            count += 1

    print(count)
