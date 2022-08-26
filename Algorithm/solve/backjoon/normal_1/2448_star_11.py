import sys


def draw_star(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    stars = draw_star(int(n/2))
    new_stars = []

    for i, item in enumerate(stars):
        new_stars.append(" "*int(n/2) + item + " "*int(n/2))

    for i, item in enumerate(stars):
        new_stars.append(item + " " + item)

    return new_stars


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    star = draw_star(n)
    for item in star:
        print(item)
