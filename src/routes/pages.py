from flask import render_template


def initialize(app):
    # Sample routes
    @app.route("/")
    def dashboard():
        return render_template('index.pug')

    @app.route("/charts")
    def charts():
        return render_template('charts.pug')

    @app.route("/tables")
    def tables():
        return render_template('tables.pug')

    @app.route("/navbar")
    def navbar():
        return render_template('navbar.pug')

    @app.route("/cards")
    def cards():
        return render_template('cards.pug')

    @app.route("/login")
    def login():
        return render_template('login.pug')

    @app.route("/register")
    def register():
        return render_template('register.pug')

    @app.route("/forgot-password")
    def forgot_password():
        return render_template('forgot-password.pug')

    @app.route("/blank")
    def blank():
        return render_template('blank.pug')
