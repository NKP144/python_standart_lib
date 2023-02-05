import argparse
parser = argparse.ArgumentParser(description="Test description")
# parser.add_argument('-n', action='store', dest='n', help='Simple value')
parser.add_argument('square', type=int, help='display a square of a given number')
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")

args = parser.parse_args()
answer = args.square**2

if args.verbose:
    print(f"the square of {args.square} is {answer}")
else:
    print(answer)
