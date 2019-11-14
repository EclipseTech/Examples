import logging


if __name__ == '__main__':
    # Setup logging
    log = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)

    # Basic
    log.debug('{} Debug level log'.format('Example 1'))
    log.info('{} Info level log'.format('Example 2'))
    log.warning('{} Warning level log'.format('Example 3'))
    log.error('{} Error level log'.format('Example 4'))
    try:
        raise Exception('This is an Exception!')
    except:
        log.exception('{} Exception is an Error level log with stack trace'.format('Example 5'))
