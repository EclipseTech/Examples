# https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/

# $ python argparseIntermediate.py hello Jef
# Hello, Jef!

# $ python argparseIntermediate.py --help
# usage: argparseIntermediate.py [-h] {hello,goodbye} ...
#
# positional arguments:
#   {hello,goodbye}
#
# optional arguments:
#   -h, --help       show this help message and exit

# $ python argparseIntermediate.py hello --help
# usage: argparseIntermediate.py hello [-h] name
#
# positional arguments:
#   name
#
# optional arguments:
#   -h, --help  show this help message and exit

import argparse


def hello(args):
    print('Hello, {0}!'.format(args.name))


def goodbye(args):
    print('Goodbye, {0}!'.format(args.name))

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

hello_parser = subparsers.add_parser('hello')
hello_parser.add_argument('name') # add the name argument
hello_parser.set_defaults(func=hello)  # set the default function to hello

goodbye_parser = subparsers.add_parser('goodbye')
goodbye_parser.add_argument('name')
goodbye_parser.set_defaults(func=goodbye)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)  # call the default function
