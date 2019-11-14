import logging
import another_module


class bad_logging2():
    def __init__(self):
        self.variable = another_module.do_something()
        logging.basicConfig(level=logging.DEBUG)

    def main(self):
        logging.debug('variable set by another_module: {}'.format(self.variable))
        logging.info('Why is this not logging? I setup logging basicConfig to DEBUG!')
        logging.warning('Oh, now it is working, what is eating my debug and info logging?')


if __name__ == '__main__':
    example = bad_logging2()
    example.main()
