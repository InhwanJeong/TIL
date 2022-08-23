import sys


def draw_star(n):
    if n == 1:
        return ['*']

    stars = draw_star(int(n/3))
    star_list = []

    for star in stars:
        star_list.append(star*3)
    for star in stars:
        star_list.append(star + ' ' * int(n/3) + star)
    for star in stars:
        star_list.append(star*3)
    return star_list


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    print('\n'.join(draw_star(n)))
