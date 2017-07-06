# https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/

# $ python clickIntermediate.py hello Jef
# Hello, Jef!

# $ python clickIntermediate.py --help
# Usage: clickIntermediate.py [OPTIONS] COMMAND [ARGS]...
#
# Options:
#   --help  Show this message and exit.
#
# Commands:
#   goodbye
#   hello

# $ python clickIntermediate.py hello --help
# Usage: clickIntermediate.py hello [OPTIONS] NAME
#
# Options:
#   --help  Show this message and exit.

import click


@click.group()
def greet():
    pass

@greet.command()
@click.argument('name') # add the name argument
def hello(**kwargs):
    print('Hello, {0}!'.format(kwargs['name']))

@greet.command()
@click.argument('name') # add the name argument
def goodbye(**kwargs):
    print('Goodbye, {0}!'.format(kwargs['name']))

if __name__ == '__main__':
    greet()
