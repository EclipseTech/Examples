import logging
import other_module


# This will not show up
# Why?
# logging.<any log level> when called for the first time will setup the root logger w/ defaults
# this will not show up because the root logger defaults are set to warning & above
logging.info('I expect this to show up')
logging.warning('This warning will show up')
logging.error('and so will this error')

# So if info or debug level is what I wan't, can't I just setup the root logger?
logging.basicConfig(level=logging.DEBUG)
# Now this should show up, right?
logging.debug('Nope')
# The root logger was already setup.
# I can change the log level though, right?
logging.getLogger().setLevel(logging.DEBUG)
logging.debug('This works now, what could go wrong?')
# Calling another module to do something
other_module.do_something()
logging.debug('Nothing can go wrong')
logging.info('Wait, why is this not logging')
logging.warning('Really... why?')
logging.error('LOG NOW, GO, DO IT! Oh, that is better')
# The other module changed the root logging level, which changes it everywhere the root logger is used
# All modules are now affected
# This is also bad because any module to import this will call all these functions that are in the global level
#    causing the root logger to be at the error level and log all of this to the console
# Now let's go look at bad_logging2.py
