import logging


if __name__ == '__main__':
    # Setup logging
    logging.basicConfig(level=logging.DEBUG)

    # Basic
    logging.debug('{} Debug level log'.format('Example 1'))
    logging.info('{} Info level log'.format('Example 2'))
    logging.warning('{} Warning level log'.format('Example 3'))
    logging.error('{} Error level log'.format('Example 4'))
    try:
        raise Exception('This is an Exception!')
    except:
        logging.exception('{} Exception is an Error level log with stack trace'.format('Example 5'))

