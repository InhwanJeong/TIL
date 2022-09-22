import sys


def make_password(location, word):
    if len(word) == l:
        vowel_count = [char for char in word if char in vowel]
        not_vowel_count = [char for char in word if char not in vowel]
        if vowel_count and len(not_vowel_count) > 1:
            print(''.join(word))
        return 0

    for j in range(location, c):
        word.append(char_list[j])
        make_password(j+1, word)
        word.pop()


if __name__ == '__main__':
    vowel = ['a', 'e', 'i', 'o', 'u']
    l, c = map(int, sys.stdin.readline().replace('\n', '').split())
    char_list = sorted(sys.stdin.readline().replace('\n', '').split())
    make_password(0, [])

"""
4 6
a t c i s w
"""