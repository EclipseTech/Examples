# https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/
import argparse


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

hello_parser = subparsers.add_parser('hello')
goodbye_parser = subparsers.add_parser('goodbye')

if __name__ == '__main__':
    args = parser.parse_args()
