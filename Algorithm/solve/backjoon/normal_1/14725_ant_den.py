import sys


class Trie:
    def __init__(self):
        self.root = {}

    def show(self):
        print(self.root)

    def get(self):
        return self.root

    def insert(self, items: list):
        current = self.root
        for string in items:
            if string not in current:
                current[string] = {}
            current = current[string]


def recur(current_trie_dict, depth):
    if not current_trie_dict:
        return 0

    for key, value in sorted(current_trie_dict.items()):
        if key != "*":
            print('-'*(depth*2) + key)
            recur(value, depth+1)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    trie = Trie()

    for _ in range(n):
        items = sys.stdin.readline().replace('\n', '').split()
        items.append("*")
        trie.insert(items[1:])

    trie_dict = trie.get()
    recur(trie_dict, 0)
