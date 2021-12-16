import logging

logger = logging.getLogger('mirror_groups')
log_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

file_handler = logging.FileHandler('mirror-groups.log')
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


'''
logger.CRITICAL()
logger.ERROR()
logger.WARNING()
logger.INFO()
logger.DEBUG()
'''