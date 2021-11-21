import random

from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO
from threading import Lock
from flask_cors import CORS

from Worker.curd import worker
from visualization.time import time_count
from visualization.today import today_Count
from visualization.disposepercent import dispose_percent
from visualization.place import place
from visualization.map import map_count
from visualization.increased import increased
from Login.logining import loginModule
from camera.Sh_curd import camera
from Worker.picture import picture
app = Flask(__name__)
CORS(app, resources='/*')
app.config['JSON_AS_ASCII'] = False
UPLOAD_FOLDER = 'static/photo'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.register_blueprint(picture, url_prefix='/picture')
app.register_blueprint(camera, url_prefix='/camera')
app.register_blueprint(loginModule, url_prefix='/loginModule')
app.register_blueprint(worker, url_prefix='/worker')
app.register_blueprint(time_count, url_prefix='/time_count')
app.register_blueprint(today_Count, uel_prefix='/today_Count')
app.register_blueprint(dispose_percent, url_prefix='/dispose_percent')
app.register_blueprint(place, url_prefix='/place')
app.register_blueprint(map_count, url_prefix='/map_count')
app.register_blueprint(increased, url_prefix='/increased')
socketIo = SocketIO(app)
thread = None
thread_lock = Lock()


@app.route('/')
def index():
    return render_template('index.html')


# @socketIo.on('connect', namespace='/test_conn')
# def test_connect():
#     global thread
#     with thread_lock:
#         if thread is None:
#             thread = socketIo.start_background_task(target=background_thread)
#
#
# def background_thread():
#     while True:
#         socketIo.sleep(5)
#         data = request.values.to_dict()
#         ret =  random.randint(1, 100)
#         socketIo.emit('server_response', {'data':data }, namespace='/test_conn')


if __name__ == '__main__':
    app.run(port=8080)
