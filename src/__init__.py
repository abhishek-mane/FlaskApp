from flask import Flask, request, send_from_directory, render_template
import jinja2

# initialize flask app
app = Flask(__name__)

# Jinja2 configurations
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
    return render_template('index.html')
