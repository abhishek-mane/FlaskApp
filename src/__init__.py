'''
    * Flask App Initialization
'''

# library imports
import logging
from flask import Flask

# custom imports
from .utils import initializeLogger
from .routes import initialize as initializeRoutes
from .web_config import CONFIG

# initializing server utilities
initializeLogger(CONFIG)

# initialize flask app
app = Flask(
    __name__,                                               # App name
    static_url_path=CONFIG['static_url_path'],          # static url path
    # folder for storing static contents
    static_folder=CONFIG['static_folder'],
    template_folder=CONFIG['template_folder'],          # folder of templates
)

# updating app configurations
logging.info('Initializing application configurations')
app.config.from_object(CONFIG['app_config'])

# using pug as template engine
logging.info('Initializing pug template engine')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

# initialize routes
logging.info('Initializing webserver routes')
initializeRoutes(app)

# initialize logger
