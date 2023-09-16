import logging


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger()

def print_error(title: str, des: str):
    logger.error(f'============={title}=============')
    logger.error(f'Details >>>: {des if des is not None else ""}')