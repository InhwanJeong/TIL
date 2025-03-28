import sys


class Trie:
    def __init__(self):
        self.root = {}
        self.nickname = {}

    def insert(self, string):
        current_node = self.root
        self.__make_nickname(string)
        for char in string:
            if char not in current_node:
                if char == "*":
                    current_node[char] = 1
                else:
                    current_node[char] = {}
            if char == "*":
                current_node[char] += 1
            current_node = current_node[char]

    def __make_nickname(self, string):
        current_node = self.root
        nickname = ''
        for char in string:
            nickname += char
            if char not in current_node:
                if char == '*':
                    nickname = nickname.replace('*', '')
                break
            current_node = current_node[char]
            if char == '*':
                if current_node == 1:
                    nickname = nickname.replace('*', '')
                else:
                    nickname = nickname.replace('*', str(current_node))
        print(nickname)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    trie = Trie()

    for _ in range(n):
        input_data = sys.stdin.readline().replace('\n', '')
        trie.insert(input_data + "*")
