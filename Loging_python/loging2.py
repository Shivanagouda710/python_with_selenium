import logging


# logging.basicConfig(level=logging.DEBUG,filename="demologs_with_time.log",filemode="w")

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
fh=logging.FileHandler("demologs_with_time.log")


# steran handler for console
# file handle to store in file
ch = logging.StreamHandler()
fh = logging.FileHandler("demologs_with_time.log")

ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')