import argparse


add_15 = lambda x: x + 15
mul = lambda x, y: x * y

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type=float)
    parser.add_argument('-y', type=float)

    return parser.parse_args()


def main():
    args = parse_args()

    x = args.x
    y = args.y

    print(add_15(x))
    print(mul(x, y))


if __name__ == "__main__":
    main()
