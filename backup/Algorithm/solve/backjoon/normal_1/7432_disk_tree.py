import sys


class Trie:
    def __init__(self):
        self.root = {}

    def get_root(self):
        return self.root

    def insert(self, path):
        current_node = self.root
        for name in path:
            if name not in current_node:
                current_node[name] = {}
            current_node = current_node[name]

    def full_search(self, current_node, count = 0):
        for key, value in sorted(current_node.items()):
            if key != "*":
                print(' ' * count + key)
                self.full_search(current_node[key], count+1)


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    trie = Trie()

    for _ in range(n):
        input_data = sys.stdin.readline().replace('\n', '').split('\\')
        input_data.append("*")
        trie.insert(input_data)

    trie.full_search(trie.get_root())
