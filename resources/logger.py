import logging

logger = logging.getLogger('mirror_groups')
logger.setLevel(logging.DEBUG) 

file_handler = logging.FileHandler('mirror-groups.log')
file_handler_format = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler.setFormatter(file_handler_format)
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler_format = logging.Formatter('(%(levelname)s) - %(message)s')
stream_handler.setFormatter(stream_handler_format)
stream_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


'''
logger.CRITICAL()
logger.ERROR()
logger.WARNING()
logger.INFO()
logger.DEBUG()
'''