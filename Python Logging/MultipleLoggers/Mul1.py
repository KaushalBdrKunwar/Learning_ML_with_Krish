import logging
## create a logger for module1
logger1 = logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

## create a logger for module2
logger2 = logging.getLogger("module2")
logger2.setLevel(logging.WARNING)

# Basic logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# log message with different loggers
logger1.debug("This is debug message for module1")
logger2.warning("This is warning message for module2")