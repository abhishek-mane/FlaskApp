'''
    * Global configurations for app
'''

import os, inspect, os.path
from src.app_config import Config, ProductionConfig, DevelopmentConfig, TestingConfig

root_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

print os.path.abspath(os.path.join(root_dir,os.pardir))

CONFIG = {
    # 'root_dir'          : '',
    'app_config'        : DevelopmentConfig,
    'host'              : 'localhost',
    'port'              : 3000,
    'static_url_path'   : '/static',
    'static_folder'     : 'public',
    'template_folder'   : 'views',
    'logging'           :{
        'console':{
            'level': 'INFO',
        },
        'file':{
            'level': 'DEBUG',
            'filename': 'server.log',
            'maxBytes': 1024*10,
            'backupCount': 3,
        }
    }
}