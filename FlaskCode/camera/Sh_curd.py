import json
from math import ceil
from settings import mysql_connect
from flask import Flask, jsonify, Blueprint, request

camera = Blueprint('camera', __name__)
conn = mysql_connect()


@camera.route('/show_camera', methods=['POST'])
def camera_all():
    cur = conn.cursor()
    data = request.data
    json_data = json.loads(data)
    partition = json_data.get("partition")
    street = json_data.get("street")
    states = json_data.get("states")
    pagesize = json_data.get("pagesize")
    pageIndex = json_data.get("pageIndex")

    sql = "select * from `摄像头表` where 1=1"

    if partition != None:
        sql = sql + " and `分区` = '" + partition + "'"
    if street != None:
        sql = sql + " and `街道` = '" + street + "'"
    if states != None:
        sql = sql + " and `状态` = '" + states + "'"

    print(sql)
    cur.execute(sql)
    content1 = cur.fetchall()
    count = len(content1)
    print(count)
    page = ceil(count/pagesize)

    sql = sql + " limit %s,%d" % (pagesize * (pageIndex - 1), pagesize)
    print(sql)
    cur.execute(sql)
    content = cur.fetchall()

    if len(content) != 0:
        msg = '获取成功'
    else:
        msg = '获取失败'

    sql = "SHOW FIELDS FROM `摄像头表`"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]
    return jsonify({'msg': msg, 'page': page, 'data': {'labels': labels, 'content': content}})


@camera.route('/add_camera', methods=['POST'])
def add_camera():
    cur = conn.cursor()
    data = request.data
    json_data = json.loads(data)
    Type = json_data.get("type")
    point = json_data.get("point")
    time = json_data.get("time")
    partition = json_data.get("partition")
    street = json_data.get("street")
    address = json_data.get("address")
    cur.execute("call camera(@num)")
    sql = "select @num"
    cur.execute(sql)
    num = cur.fetchall()
    id = num[0][0]

    print(id)
    sql1 = "insert into `摄像头表`(`摄像头编号`,`坐标`,`分区`,`街道`,`地点`,`状态`,`添加时间`,`型号`)" \
           "values('%s','%s','%s','%s','%s',%s,'%s','%s')" %(id, point, partition, street,
                                                    address, "1", time, Type)
    cur.execute(sql1)
    return jsonify({})


@camera.route('/delete_camera', methods=['POST'])
def delete_camera():
    cur = conn.cursor()
    data = request.data
    json_data = json.loads(data)
    id = json_data.get("id")
    sql = "delete from `摄像头表` where `摄像头编号`='" + id + "'"
    result = cur.execute(sql)
    if result == 1:
        msg = '操作成功'
    else:
        msg = '操作失败'
    return jsonify({'msg': msg})


@camera.route('/edit_camera', methods=['POST'])
def edit_camera():
    cur = conn.cursor()
    data = request.data
    json_data = json.loads(data)
    id = json_data.get("id")
    states = json_data.get("states")
    msg = '修改失败'
    if states !=None:
        sql = "UPDATE `摄像头表` SET `状态`= %s where `摄像头编号`= '%s'" %(states, id)
        result = cur.execute(sql)
        print(sql)
        print(result)
        if result == 1:
            msg = '修改成功'
        else:
            msg = '修改失败'

    return jsonify({'msg': msg})

