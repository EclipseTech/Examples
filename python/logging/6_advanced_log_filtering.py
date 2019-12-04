import logging
import re


# Modified from https://relaxdiego.com/2014/07/logging-in-python.html
class RedactFilter(logging.Filter):
    default_filter = ['(password|passwd|pass|token)(\s*)?([=|:]*)']

    def __init__(self, filter_prefix_regexes=default_filter):
        super(RedactFilter, self).__init__()
        self.__prefixes = filter_prefix_regexes

    def filter(self, record):
        record.msg = self.redact(record.msg)
        if isinstance(record.args, dict):
            for key in record.args.keys():
                record.args[key] = self.redact(record.args[key])
        else:
            record.args = tuple(self.redact(arg) for arg in record.args)
        return True

    def redact(self, msg):
        msg = isinstance(msg, basestring) and msg or str(msg)
        for prefix in self.__prefixes:
            if re.match(prefix, msg):
                # regex replace `regex<any spaces>(first word)` become `regex<any spaces><<REDACTED>>` maintaining spaces
                msg = re.sub(r'({}\s*)(\w*)'.format(prefix), r'\1<<REDACTED>>'.format(prefix), msg)
        return msg


if __name__ == '__main__':
    # Setup logging
    log = logging.getLogger(__name__)
    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter('%(levelname)-8s %(message)s')
    stream_handler.setFormatter(stream_formatter)
    stream_handler.addFilter(RedactFilter())
    log.addHandler(stream_handler)
    log.setLevel(logging.DEBUG)

    # Again with the basic log example
    # However this time it is going to filter any characters between prefix and the next space
    log.debug('{} Debug level log'.format('passwd 1'))
    log.info('{} Info level log'.format('pass: 2'))
    log.warning('{} Warning level log'.format('password = 3'))
    log.error('{} Error level log'.format('token : 4'))
    try:
        raise Exception('This is an Exception!')
    except:
        log.exception('{} Exception is an Error level log with stack trace'.format('password=5'))

    # Setup logging example 2 filtering the number coming after example in this case
    log2 = logging.getLogger(__name__ + '2')
    stream_handler = logging.StreamHandler()
    stream_handler.addFilter(RedactFilter(['Example']))
    log2.addHandler(stream_handler)
    log2.setLevel(logging.DEBUG)

    # Again with the basic log example
    # However this time it is going to filter any characters between prefix and the next space
    log2.debug('{} Debug level log'.format('Example 1'))
    log2.info('{} Info level log'.format('Example 2'))
    log2.warning('{} Warning level log'.format('Example 3'))
    log2.error('{} Error level log'.format('Example 4'))
    try:
        raise Exception('This is an Exception!')
    except:
        log2.exception('{} Exception is an Error level log with stack trace'.format('Example 5'))
    log2.critical('{} Critical level log'.format('Example 6'))
