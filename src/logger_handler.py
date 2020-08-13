import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    format='[%(asctime)-15s][%(levelname)s] {%(filename)s : %(funcName)s : %(lineno)d}  - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)


def get_logger(name: str) -> logging:
    return logging.getLogger(name)
