'''
    * Logger initialization module
'''

import logging.config

def initialize(CONFIG):
    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }
        },
        'handlers': {
            'console': {
                'class'         : 'logging.StreamHandler',
                'formatter'     : 'default',
                'stream'        : 'ext://sys.stdout',
                'level'         : CONFIG['logging']['console']['level'],
            },
            'file': {
                'class'         : 'logging.handlers.RotatingFileHandler',
                'formatter'     : 'default',
                'filename'      : CONFIG['logging']['file']['filename'],
                'maxBytes'      : CONFIG['logging']['file']['maxBytes'],
                'backupCount'   : CONFIG['logging']['file']['backupCount'],
                'level'         : CONFIG['logging']['file']['level'],
            },
        },
        'root': {
            'level' : 'INFO',
            'handlers': ['console', 'file']
        }
    })
