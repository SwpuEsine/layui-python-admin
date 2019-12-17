from .main_view import main_view


def init_app(app):
    app.register_blueprint(main_view)
