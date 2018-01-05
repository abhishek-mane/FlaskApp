'''
    * Setup required configurations for flask
'''


def initializeLogger(CONFIG):
    from . import logger
    logger.initialize(CONFIG)


def initializeErrorPages(app):
    from . import errors
    errors.initialize(app)
