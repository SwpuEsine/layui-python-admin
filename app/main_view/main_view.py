# coding: utf-8
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL
from flask import Blueprint, render_template, request

main_view = Blueprint('main_view', __name__)


# 主页面
@main_view.route('/')
def show():
    return render_template("index.html")


# 页面跳转
@main_view.route('/html_page')
def html_page():
    new_url = request.values.get("new_url") + ".html"
    return render_template(new_url)


@main_view.route('/upload', methods=['POST', 'GET'])
def upload():
    photos = UploadSet('PHOTO')
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return "show"
    return ""
