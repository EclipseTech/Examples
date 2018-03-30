import logging


# Setup logging
log = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)-8s %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)


log.info("Example info level log: {0}".format("Test 1"))
log.debug("Example debug level log: {0}".format("Test 2"))
