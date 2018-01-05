'''
    * Flask App Initialization
'''

# library imports
import os, inspect, os.path
import logging
from flask import Flask

# custom imports
from .utils import initializeLogger
from .routes import initialize as initializeRoutes
from .web_config import CONFIG

# initializing logger
initializeLogger(CONFIG)

# initialize flask app
app = Flask(
    CONFIG['name'],
    static_url_path = '/static',
    static_folder   = 'public',
    template_folder = 'views',
    root_path       = CONFIG['APP_DIR']
)

# app.config is pending

# using pug as template engine
logging.info('Initializing pug template engine')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

# initialize routes
logging.info('Initializing webserver routes')
initializeRoutes(app)