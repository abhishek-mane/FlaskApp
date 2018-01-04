'''
    * Flask app configurations
'''

class Config(object):
    ''' Basic flask app configurations '''
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    ''' Production configurations '''

class DevelopmentConfig(Config):
    ''' Development configurations '''
    TEMPLATES_AUTO_RELOAD = True
    DEBUG = True

class TestingConfig(Config):
    ''' Testing configurations '''
    TEMPLATES_AUTO_RELOAD = True
    TESTING = True
