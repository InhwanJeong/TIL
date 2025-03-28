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

    def search_auto(self, string):
        current = self.root
        length = len(string)
        count = 0
        i = 0
        while i <= length - 1:
            count += 1
            if string[i] in current:
                current = current[string[i]]
            i += 1
            while len(current.keys()) == 1:
                if '*' in current.keys():
                    break
                if string[i] in current:
                    current = current[string[i]]
                    i += 1
        return count


if __name__ == '__main__':
    while True:
        try:
            test_case = int(sys.stdin.readline())
            word_list = [sys.stdin.readline().replace('\n', '') for _ in range(test_case)]
            trie = Trie()

            for word in word_list:
                trie.insert(word + "*")

            click = 0
            for word in word_list:
                click += trie.search_auto(word)

            print(f'{click/len(word_list):.2f}')

        except Exception as e:
            break

"""
4
hello
hell
heaven
goodbye
3
hi
he
h
7
structure
structures
ride
riders
stress
solstice
ridiculous
"""