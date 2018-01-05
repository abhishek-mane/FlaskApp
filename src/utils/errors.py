from flask import render_template


def initialize(app):
    @app.errorhandler(401)
    def unauthorized(e):
        return render_template('401.html')

    @app.errorhandler(400)
    def bad_request(e):
        return render_template('400.html')

    @app.errorhandler(404)
    def not_found(e):
        return render_template('error_pages/404.html')

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html')
