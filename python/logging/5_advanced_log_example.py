import logging


class LoggingLevelFilter(logging.Filter):
    def __init__(self, levels):
        self.__levels = levels

    def filter(self, log):
        return log.levelno in self.__levels


if __name__ == '__main__':
    # Setup logging
    log = logging.getLogger(__name__)
    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter('%(levelname)-8s %(message)s')
    stream_handler.setFormatter(stream_formatter)
    log.addHandler(stream_handler)
    log.setLevel(logging.DEBUG)

    file_format = '%(asctime)-8s %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S %Z'
    file_handler_format = logging.Formatter(fmt=file_format, datefmt=date_format)

    # Just log debug level to a 'debug.log'
    debug_file_handler = logging.FileHandler('debug.log')
    debug_file_handler.setFormatter(file_handler_format)
    debug_file_handler.addFilter(LoggingLevelFilter([logging.DEBUG]))
    log.addHandler(debug_file_handler)

    # Just log warning and error levels to a 'warning_and_error.log'
    warn_error_file_handler = logging.FileHandler('warning_and_error.log')
    warn_error_file_handler.setFormatter(file_handler_format)
    warn_error_file_handler.addFilter(LoggingLevelFilter([logging.WARNING, logging.ERROR, logging.CRITICAL]))
    log.addHandler(warn_error_file_handler)

    # Again with the basic log example
    # However this time it is going to log debug, warnings and errors to their own files
    # Info and above will be printed to the console
    log.debug('{} Debug level log'.format('Example 1'))
    log.info('{} Info level log'.format('Example 2'))
    log.warning('{} Warning level log'.format('Example 3'))
    log.error('{} Error level log'.format('Example 4'))
    try:
        raise Exception('This is an Exception!')
    except:
        log.exception('{} Exception is an Error level log with stack trace'.format('Example 5'))
    log.critical('{} Critical level log'.format('Example 6'))
