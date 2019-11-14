import logging


def do_something():
    # Errors should be the only logging anyone ever sees from my module
    logging.getLogger().setLevel(logging.ERROR)
