'''
    * Flask App Initialization
'''

import jinja2
from flask import Flask, request, send_from_directory, render_template
from src.web_config import WEBCONFIG as CONFIG

# initialize flask app
APP = Flask(
    __name__,                                           # App name
    static_url_path=CONFIG['static_url_path'],          # static url path
    static_folder=CONFIG['static_folder'],              # folder for storing static contents
    template_folder=CONFIG['template_folder'],          # folder of templates
)

APP.config.from_object(CONFIG['app_config'])

# Jinja2 configurations
APP.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

# Sample routes
@APP.route("/")
def dashboard():
    return render_template('index.pug')


@APP.route("/charts.html")
def charts():
    return render_template('charts.pug')


@APP.route("/tables.html")
def tables():
    return render_template('tables.pug')


@APP.route("/navbar.html")
def navbar():
    return render_template('navbar.pug')


@APP.route("/cards.html")
def cards():
    return render_template('cards.pug')


@APP.route("/login.html")
def login():
    return render_template('login.pug')


@APP.route("/register.html")
def register():
    return render_template('register.pug')


@APP.route("/forgot-password.html")
def forgot_password():
    return render_template('forgot-password.pug')


@APP.route("/blank.html")
def blank():
    return render_template('blank.pug')
