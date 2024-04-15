import logging
import logger
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# Configuramos el logger
logging.basicConfig(level=logging.DEBUG, format='{ \'time\': \'%(asctime)s\', \'name\': \'%(name)s\', \'level\': \'%(levelname)s\', \'message\': \'%(message)s\', \'filename\': \'%(filename)s\', \'module\': \'%(module)s\', \'processName\': \'%(processName)s\', \'process\': \'%(process)d\', \'thread\': \'%(thread)d\', \'threadName\': \'%(threadName)s\', \'lineno\': \'%(lineno)d\', \'funcName\': \'%(funcName)s\', \'pathname\': \'%(pathname)s\' }', filename='log.log')

def info(message):
    logger.info(message)

def debug(message):
    logger.debug(message)

def error(message):
    logger.error(message)

def warning(message):
    logger.warning(message)

def critical(message):
    logger.critical(message)

def exception(message):
    logger.exception(message)
