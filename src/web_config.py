'''
    * Global configurations for app
'''

import os, inspect, os.path as path

APP_DIR     = path.dirname(path.abspath(inspect.getfile(inspect.currentframe())))
BASE_DIR    = path.abspath(path.join(APP_DIR,os.pardir))
LOGS_DIR    = path.join(BASE_DIR, 'logs')

CONFIG = {
    'name'                  : 'Sample Flask App',
    'host'                  : 'localhost',
    'port'                  : 8000,
    'static_url_path'       : '/static',
    'static_folder'         : 'public',
    'template_folder'       : 'views',
    'logging': {
        'console': {
            'level'         : 'INFO',
        },
        'file':{
            'level'         : 'DEBUG',
            'filename'      : path.join(LOGS_DIR, 'server.log'),
            'maxBytes'      : 1024*10,
            'backupCount'   : 3,
        }
    }
}