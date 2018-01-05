'''
    * Setup required configurations for flask
'''

def initializeLogger(CONFIG):
    from . import logger
    logger.initialize(CONFIG)
