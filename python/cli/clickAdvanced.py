# https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/

# $ python clickAdvanced.py -h
# Usage: clickAdvanced.py [OPTIONS] COMMAND [ARGS]...
#
# Options:
#   --version   Show the version and exit.
#   -h, --help  Show this message and exit.
#
# Commands:
#   goodbye
#   hello

# $ python clickAdvanced.py hello -h
# Usage: clickAdvanced.py hello [OPTIONS] NAME
#
# Options:
#   --greeting TEXT
#   --caps
#   -h, --help       Show this message and exit.

# $ python clickAdvanced.py hello --greeting "What's Up" Jef
# What's Up, Jef!

# $ python clickAdvanced.py --version
# clickAdvanced.py, version 1.0.0

import click


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def greeter(**kwargs):
    output = '{0}, {1}!'.format(kwargs['greeting'],
                                kwargs['name'])
    if kwargs['caps']:
        output = output.upper()
    print(output)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='1.0.0')
def greet():
    pass


@greet.command()
@click.argument('name')
# add an option with 'Hello' as the default
@click.option('--greeting', default='Hello')
# add a flag (is_flag=True)
@click.option('--caps', is_flag=True)
# the application logic has been refactored into a single function
def hello(**kwargs):
    greeter(**kwargs)


@greet.command()
@click.argument('name')
@click.option('--greeting', default='Goodbye')
@click.option('--caps', is_flag=True)
def goodbye(**kwargs):
    greeter(**kwargs)

if __name__ == '__main__':
    greet()
