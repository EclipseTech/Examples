import logging


class i_am_a_log_hog():
    def __init__(self):
        log = logging.getLogger(__name__)
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter('%(levelname)-8s:{} %(message)s'.format(__name__))
        stream_handler.setFormatter(stream_formatter)
        log.addHandler(stream_handler)
        log.setLevel(logging.DEBUG)
        log.debug('I set up my log nicely')

    def do_something(self):
        log.debug('I am doing something and logging to everyones console')
