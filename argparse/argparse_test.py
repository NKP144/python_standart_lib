import argparse
parser = argparse.ArgumentParser(description="Test description")
# parser.add_argument('-n', action='store', dest='n', help='Simple value')
group = parser.add_mutually_exclusive_group()
parser.add_argument('square', type=int, help='display a square of a given number')
# parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
# parser.add_argument("-v", "--verbose", type=int, choices=[0, 1], help="increase output verbosity")
# parser.add_argument("-q", "--quiet", action="store_true")

group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

args = parser.parse_args()
answer = args.square**2

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"Running {__file__}")
    print(f"the square of {args.square} is {answer}")
else:
    print(f"{args.square}^2 == {answer}")
