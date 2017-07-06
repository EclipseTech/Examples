# https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/

# $ python argparseAdvanced.py -h
# usage: argparseAdvanced.py [-h] {hello,goodbye} ...
#
# positional arguments:
#   {hello,goodbye}
#
# optional arguments:
#   -h, --help       show this help message and exit
#   --version        show program's version number and exit

# $ python argparseAdvanced.py hello -h
# usage: argparseAdvanced.py hello [-h] [--greeting GREETING] [--caps] name
#
# positional arguments:
#   name
#
# optional arguments:
#   -h, --help           show this help message and exit
#   --greeting GREETING
#   --caps

# $ python argparseAdvanced.py hello --greeting "What's Up" Jef
# What's Up, Jef!

# $ python argparseAdvanced.py --version
# 1.0.0

import argparse


# since we are now passing in the greeting
# the logic has been consolidated to a single greet function
def greet(args):
    output = '{0}, {1}!'.format(args.greeting, args.name)
    if args.caps:
        output = output.upper()
    print(output)

parser = argparse.ArgumentParser()
# Add version argument (hard coded version)
parser.add_argument('--version', action='version', version='1.0.0')
subparsers = parser.add_subparsers()

hello_parser = subparsers.add_parser('hello')
hello_parser.add_argument('name')
# add greeting option w/ default
hello_parser.add_argument('--greeting', default='Hello')
# add a flag (default=False)
hello_parser.add_argument('--caps', action='store_true')
hello_parser.set_defaults(func=greet)

goodbye_parser = subparsers.add_parser('goodbye')
goodbye_parser.add_argument('name')
goodbye_parser.add_argument('--greeting', default='Goodbye')
goodbye_parser.add_argument('--caps', action='store_true')
goodbye_parser.set_defaults(func=greet)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
