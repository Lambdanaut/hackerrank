import sys

def solve(children):
    children_len = len(children)
    children_candies = [1 for child in children]
    pointer = 0

    while True:
        c_ch = children[pointer]
        c_ca = children_candies[pointer]
        if pointer == 0: p_ch = None
        else:            p_ch = children[pointer-1]
        try:    n_ch = children[pointer+1]
        except: n_ch = None

        if p_ch:
            p_ca = children_candies[pointer-1]

            if c_ch > p_ch and c_ca <= p_ca:
                children_candies[pointer] += 1
                continue
            elif c_ch < p_ch and c_ca >= p_ca:
                pointer -= 1
                continue

        if n_ch:
            n_ca = children_candies[pointer+1]

            if c_ch > n_ch and c_ca <= n_ca:
                children_candies[pointer] += 1
                continue
            else:
                pointer += 1
                continue

        else:
            return sum(children_candies)

        pointer += 1


def main():
    # Read input from a file if one is provided
    # Else read from stdin
    try:
        filename = sys.argv[1]
        data = open(filename, 'rb').readlines()
    except IndexError:
        data = sys.stdin.readlines()

    # Extract constants from input
    children = [int(v) for v in data[1:]]

    answer = solve(children)

    if answer:
        print(answer)


if __name__ == '__main__':
    main()
