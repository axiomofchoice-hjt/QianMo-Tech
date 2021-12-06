import json

from flask import Blueprint, jsonify, request
from settings import mysql_connect

user_complain = Blueprint('user_complain', __name__)
conn = mysql_connect()
cur = conn.cursor()


@user_complain.route('/user_complain', methods=['POST'])
def usr_complain():
    data = request.data
    json_data = json.loads(data)
    index = json_data.get("index")
    message = json_data.get("message")
    pic = json_data.get("pic")
    return_msg = json_data.get("return_msg")
    result = json_data.get("result")
    sql = "insert into `事件申诉表`(`事件编号`,`申诉内容`,`上传图片`,`申诉结果`,`备注`)" \
          "values('%s','%s','%s','%s','%s')" % (index, message, pic, result, return_msg)
    cur.execute(sql)
    print(sql)
    return jsonify({})


@user_complain.route('/get_complain', methods=['POST'])
def get_comp():
    data = request.data
    json_data = json.loads(data)
    index = json_data.get("index")
    sql = "select * from `事件申诉表` where `事件编号`= '" + index + "'"
    print(sql)
    re = cur.execute(sql)
    print(re)
    content = cur.fetchall()
    msg = ""
    if re != 0:
        msg = "获取成功"
    else:
        msg = "获取失败"
    return jsonify({"content": content, "msg": msg})


@user_complain.route('/edit_complain', methods=['POST'])
def edit():
    data = request.data
    json_data = json.loads(data)
    index = json_data.get("index")
    result = json_data.get("result")
    return_msg = json_data.get("return_msg")

    sql = "UPDATE `事件申诉表` SET `事件编号`= '%s', `申诉结果`= %s,`备注`= '%s'"\
          % (index, result, return_msg)

    print(sql)
    cur.execute(sql)
    return jsonify({})






