'''
    * Flask App Initialization
'''

# library imports
import os, inspect, os.path
import logging
from flask import Flask

# custom imports
from .utils import initializeLogger, initializeErrorPages
from .views import initialize as initializeViews
from .web_config import CONFIG

# initializing logger
initializeLogger(CONFIG)

# initialize flask app
app = Flask(
    CONFIG['name'],
    static_url_path = CONFIG['static_url_path'],
    static_folder   = CONFIG['static_folder'],
    template_folder = CONFIG['template_folder'],
    root_path       = CONFIG['APP_DIR']
)

# app.config is pending

# using pug as template engine
logging.info('Initializing pug template engine')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

# initialize routes
logging.info('Initializing webserver routes')
initializeViews(app)

# initialize utils
initializeErrorPages(app)