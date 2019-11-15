import logging
import log_hog


if __name__ == '__main__':
    # Setup logging
    log = logging.getLogger(__name__)
    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter('%(levelname)-8s:{} %(message)s'.format(__name__))
    stream_handler.setFormatter(stream_formatter)
    log.addHandler(stream_handler)
    log.setLevel(logging.INFO)

    log.info('I setup my log nicely')
    hog = log_hog.i_am_a_log_hog()
    hog.do_something()
