# https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/

# $ python docoptIntermediate.py hello Jef
# Hello, Jef!

# $ python docoptIntermediate.py --help
# Greeter.
#
# Usage:
#   commands.py hello <name>
#   commands.py goodbye <name>
#   commands.py (-h | --help)
#
#   Options:
#     -h --help     Show this screen.


# $ python docoptIntermediate.py hello --help
# Greeter.
#
# Usage:
#   commands.py hello <name>
#   commands.py goodbye <name>
#   commands.py (-h | --help)
#
# Options:
#   -h --help     Show this screen.

"""Greeter.

Usage:
  commands.py hello <name>
  commands.py goodbye <name>
  commands.py (-h | --help)

Options:
  -h --help     Show this screen.
"""
from docopt import docopt


def hello(name):
    print('Hello, {0}!'.format(name))


def goodbye(name):
    print('Goodbye, {0}!'.format(name))

if __name__ == '__main__':
    arguments = docopt(__doc__)

    # if an argument called hello was passed, execute the hello logic.
    if arguments['hello']:
        hello(arguments['<name>'])
    elif arguments['goodbye']:
        goodbye(arguments['<name>'])
