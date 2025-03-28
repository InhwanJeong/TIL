import sys

if __name__ == '__main__':
    m = int(sys.stdin.readline())

    s = 0
    variable = 0
    bit_mask = {
        'all': lambda x: (1 << 21) - 1,
        'empty': lambda x: 0,
        'check': lambda x: s,
        'add': lambda x: s | (1 << x),
        'remove': lambda x: s & ~(1 << x),
        'toggle': lambda x: s ^ (1 << x)
    }

    for i in range(m):
        input_data = sys.stdin.readline().replace("/n", "").split()
        variable = int(input_data[-1]) if len(input_data) > 1 else 0

        s = bit_mask[input_data[0]](variable)

        if input_data[0] == 'check':
            print(1 if s & (1 << variable) != 0 else 0)
