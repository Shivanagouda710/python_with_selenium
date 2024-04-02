# DEBUG
# Detailed information, typically of interest only when diagnosing problems.

# INFO
# Confirmation that things are working as expected.

# WARNING (By default)
# An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR
# Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL
# A serious error, indicating that the program itself may be unable to continue running.

import logging

logging.basicConfig(level=logging.DEBUG,filename="demologs.log",filemode="a")

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')

logging.debug("this is debug")
logging.info("this is info")
logging.warning("this is warning")
logging.error("this is error")
logging.critical("this is critical")


