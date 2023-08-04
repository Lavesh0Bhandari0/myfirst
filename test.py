from argparse import ArgumentParser, Namespace

parser = ArgumentParser()
parser.add_argument("square", help="Squares a given number", type=int)
parser.add_arguments(
    "-v",
    "--verbose",
    help="Provides a verbose desc",
    action="store_true",
    type=int,
    choice=[0, 1, 2],
)
args: Namespace = parser.parse_args()
if args.verbose:
    print(f"{args.square} squared is: {args.square** 2}")
else:
    print(args.square**2)
