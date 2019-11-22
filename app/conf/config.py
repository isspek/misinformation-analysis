import configparser
import sys
import os
from loguru import logger

logger.add(sys.stdout, format="{time} - {level} - {message}", filter="sub.module")

# Load the configuration file
config = configparser.RawConfigParser(allow_no_value=True)
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))

# List all contents
logger.info("List all contents:")
for section in config.sections():
    logger.info("Section: %s" % section)
    for options in config.options(section):
        logger.info("x %s:::%s:::%s" % (options,
                                  config.get(section, options),
                                  str(type(options))))

# Print some contents
logger.info("\nPrint some contents")
logger.info(config.get('API', 'claimbuster'))  # Just get the value