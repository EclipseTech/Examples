# https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/
import click


@click.group()
def greet():
    pass

@greet.command()
def hello(**kwargs):
    pass

@greet.command()
def goodbye(**kwargs):
    pass

if __name__ == '__main__':
    greet()
