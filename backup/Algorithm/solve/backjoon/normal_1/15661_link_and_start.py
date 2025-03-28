import sys
import itertools


def get_team_score(start_people, r):
    if len(start_people) == r:
        link_people = [i for i, item in enumerate(visited) if not item]
        start_team = list(itertools.permutations(start_people, 2))
        link_team = list(itertools.permutations(link_people, 2))
        start_score = sum([board[i][j] for i, j in start_team])
        link_score = sum([board[i][j] for i, j in link_team])
        score_list.append(abs(start_score-link_score))
        return 0

    start = start_people[-1] if start_people else 0
    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = 1
        start_people.append(i)
        get_team_score(start_people, r)
        item = start_people.pop()
        visited[item] = 0


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().replace('\n', '').split())) for _ in range(n)]
    score_list = [100*n]
    visited = [0]*n

    for a in range(2, n//2+1):
        get_team_score([], a)

    print(min(score_list))
