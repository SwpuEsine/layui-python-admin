from flask import Flask, render_template
from werkzeug.exceptions import HTTPException


def create_app(config_name=None):
    import main_view
    app = Flask(__name__)
    # main_view 接口 根地址　/main_view

    main_view.init_app(app)

    @app.errorhandler(Exception)
    def all_exception_handler(e):
        if isinstance(e, HTTPException):
            return render_template(f"error/{e.code}.html")
        return render_template(f"error/500.html")

    return app


app = create_app()
app.run(debug=True)
