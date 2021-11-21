import os
import datetime
import random
from werkzeug.utils import secure_filename
from flask import current_app
from flask import Flask, jsonify, Blueprint, request, make_response, send_from_directory

picture = Blueprint('picture', __name__)
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
path = basedir + "/static/photo/"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])


class Pic_str:
    def create_uuid(self):
        nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        randomNum = random.randint(0, 100)
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum)
        uniqueNum = str(nowTime) + str(randomNum)
        return uniqueNum


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@picture.route('/getImg', methods=['POST'], strict_slashes=False)
def getImg():
    file_dir = os.path.join(basedir, current_app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['photo']
    print(f)
    if f and allowed_file(f.filename):
        print(f.filename)
        fname = secure_filename("1" + f.filename)
        print(fname)
        ext = fname.rsplit('.', 1)[1]
        new_filename = Pic_str().create_uuid() + '.' + ext
        f.save(os.path.join(file_dir, new_filename))

        return jsonify({"success": 0, "filename": new_filename, "msg": "上传成功"})
    else:
        return jsonify({"error": 1001, "msg": "上传失败"})


@picture.route('/download/<string:filename>', methods=['GET'])
def download(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join('static/photo', filename)):
            return send_from_directory('static/photo', filename, as_attachment=True)
        pass


# show photo
@picture.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = os.path.join(basedir, current_app.config['UPLOAD_FOLDER'])
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
    else:
        pass
