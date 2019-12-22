import os
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL
from flask import Flask, render_template, request, send_from_directory
from werkzeug.exceptions import HTTPException


def create_app(config_name=None):
    import main_view
    app = Flask(__name__)
    # main_view 接口 根地址　/main_view
    # 获取文件路径
    app.config['UPLOADED_PHOTO_DEST'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/photo_files"

    app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES

    photos = UploadSet('PHOTO')
    configure_uploads(app, photos)

    main_view.init_app(app)
    #上传页面


    @app.route("/download", methods=['GET'])
    def download_file():
        # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
        directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/photo_files"
        return send_from_directory(directory, "阿.txt", as_attachment=True)
    # 错误页面
    @app.errorhandler(Exception)
    def all_exception_handler(e):
        if isinstance(e, HTTPException):
            return render_template(f"error/{e.code}.html")
        return render_template(f"error/500.html")

    return app


app = create_app()
app.run(debug=True)
