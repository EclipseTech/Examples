import logging


# Advanced "Exception instead of Error & other exception related"
class CustomExceptionExample(BaseException):
    '''
    Exceptions mostly inherit from Exception
    However Exception and possibly other exceptions inherit from BaseException
        `except Exception:` would only catch exceptions that inherit from Exception
    Instead of using `except Exception:` to catch all exceptions, just `except:` should be used
    '''
    pass


if __name__ == '__main__':
    # Setup logging
    log = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)

    try:
        raise CustomExceptionExample('This is an instance of BaseException, not Exception')
    except Exception as e:
        # Don't do this, use .exception instead to print the stack trace
        # Also stop using `except Exception as e:` as the catch-all
        log.error('This will be ignored, error: {}'.format(e))
    except:
        log.exception('Caught instance of BaseException')
