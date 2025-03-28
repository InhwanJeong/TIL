import sys

if __name__ == '__main__':
    tired, throughput, rest, burnout = map(int, sys.stdin.readline().replace('\n', '').split())

    my_tiredness = 0
    all_throughput = 0

    for _ in range(24):
        if my_tiredness + tired <= burnout and tired <= burnout:
            my_tiredness += tired
            all_throughput += throughput
        else:
            my_tiredness -= rest
            my_tiredness = my_tiredness if my_tiredness > 0 else 0
    print(all_throughput)
