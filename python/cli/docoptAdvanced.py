# https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/

# $ python docoptAdvanced.py -h
# usage: greet [--help] <command> [<args>...]
#
# options:
#   -h --help         Show this screen.
#   --version         Show the version.
#
# commands:
#    hello       Say hello
#    goodbye     Say goodbye

# $ python docoptAdvanced.py hello -h
# usage: basic.py hello [options] [<name>]
#
#   -h --help         Show this screen.
#   --caps            Uppercase the output.
#   --greeting=<str>  Greeting to use [default: Hello].

# $ python docoptAdvanced.py hello --greeting "What's up" Jef
# What's up, Jef!

# $ python docoptAdvanced.py hello --greeting "What's up" Jef --caps
# WHAT'S UP, JEF!

# $  python docoptAdvanced.py --version
# 1.0.0

"""usage: greet [--help] <command> [<args>...]

options:
  -h --help         Show this screen.
  --version         Show the version.

commands:
   hello       Say hello
   goodbye     Say goodbye

"""
from docopt import docopt

HELLO = """usage: basic.py hello [options] [<name>]

  -h --help         Show this screen.
  --caps            Uppercase the output.
  --greeting=<str>  Greeting to use [default: Hello].
"""

GOODBYE = """usage: basic.py goodbye [options] [<name>]

  -h --help         Show this screen.
  --caps            Uppercase the output.
  --greeting=<str>  Greeting to use [default: Goodbye].
"""


def greet(args):
    output = '{0}, {1}!'.format(args['--greeting'],
                                args['<name>'])
    if args['--caps']:
        output = output.upper()
    print(output)


if __name__ == '__main__':
    arguments = docopt(__doc__, options_first=True, version='1.0.0')

    if arguments['<command>'] == 'hello':
        greet(docopt(HELLO))
    elif arguments['<command>'] == 'goodbye':
        greet(docopt(GOODBYE))
    else:
        exit("{0} is not a command. \
              See 'options.py --help'.".format(arguments['<command>']))
