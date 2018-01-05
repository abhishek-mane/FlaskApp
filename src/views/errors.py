from flask import render_template


def initialize(app):
    @app.errorhandler(401)
    def unauthorized(e):
        return render_template('401.pug')

    @app.errorhandler(400)
    def bad_request(e):
        return render_template('400.pug')

    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.pug')

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.pug')
