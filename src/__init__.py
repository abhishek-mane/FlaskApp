'''
    * Flask App Initialization
'''

# Library imports
import jinja2
from flask import Flask, request, send_from_directory, render_template

# Custom imports
from src.routes import initializeRoutes
from src.web_config import WEBCONFIG as CONFIG

# initialize flask app
app = Flask(
    __name__,                                           # App name
    static_url_path=CONFIG['static_url_path'],          # static url path
    static_folder=CONFIG['static_folder'],              # folder for storing static contents
    template_folder=CONFIG['template_folder'],          # folder of templates
)

app.config.from_object(CONFIG['app_config'])

# Pug templating
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

# initialize routes
initializeRoutes(app)