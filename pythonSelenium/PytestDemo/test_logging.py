# how to log using python

import logging

def test_logging():
    logger = logging.getLogger(__name__)


    fileHandler = logging.FileHandler("logFile.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Print Information messages")
    logger.warning("Something is in the warning mode")
    logger.error("A major error has happened")
    logger.critical("some critical information")