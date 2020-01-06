import logging


if __name__ == '__main__':
    # Setup logging name
    log = logging.getLogger(__name__)
    # Setup where logging prints output (using stdout and stderr by default)
    handler = logging.StreamHandler()
    # Setup log formatting
    formatter = logging.Formatter('%(levelname)-8s %(message)s')
    # Add formatter to the stream handler
    handler.setFormatter(formatter)
    # Add stream handler to the logger
    log.addHandler(handler)
    # Setup the logging level
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

    log.critical('{} Critical level log'.format('Example 6'))
