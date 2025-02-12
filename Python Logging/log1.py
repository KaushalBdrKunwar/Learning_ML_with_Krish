# Logging is crucial aspect of any app, providing a way to track events,
# and operational information. Pythons built-in logging module offers a flexible framework
# for emitting log messages from Python programs. In this lesson, we will cover the basics of 
#logging

import logging 

# ## Configure the basics logging settings
# logging.basicConfig(level=logging.DEBUG)

# #log messages with different severity levels
# logging.debug("This is a debug message")
# logging.info("This is info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

## Configuring logging
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

#log messages with different severity levels
logging.debug("This is a debug message")
logging.info("This is info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
