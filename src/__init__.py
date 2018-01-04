from flask import Flask, request, send_from_directory, render_template
import jinja2

# initialize flask app
app = Flask(__name__, static_url_path='')

# Jinja2 configurations
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
# app.jinja_loader = jinja2.ChoiceLoader([
#     app.jinja_loader,
#     jinja2.FileSystemLoader(['/flaskapp/userdata',
#                              '/flaskapp/templates']),
# ])

# Static server configurations
@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('public', path)

# Sample routes
@app.route("/")
def dashboard():
    return render_template('index.pug')

@app.route("/charts.html")
def charts():
    return render_template('charts.pug')

@app.route("/tables.html")
def tables():
    return render_template('tables.pug')

@app.route("/navbar.html")
def navbar():
    return render_template('navbar.pug')

@app.route("/cards.html")
def cards():
    return render_template('cards.pug')

@app.route("/login.html")
def login():
    return render_template('login.pug')

@app.route("/register.html")
def register():
    return render_template('register.pug')

@app.route("/forgot-password.html")
def forgot_password():
    return render_template('forgot-password.pug')

@app.route("/blank.html")
def blank():
    return render_template('blank.pug')