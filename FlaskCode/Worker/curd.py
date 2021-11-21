import json
from math import ceil
from settings import mysql_connect
from flask import Flask, jsonify, Blueprint, request
import pymysql

worker = Blueprint('worker', __name__)
conn = mysql_connect()


@worker.route('/show_illegal', methods=['POST'])
def illegal_all():
    data = request.data
    json_data = json.loads(data)
    from_time = json_data.get("from_time")
    to_time = json_data.get("to_time")
    partition = json_data.get("partition")
    illegal_nature = json_data.get("illegal_nature")
    states = json_data.get("states")
    carPlate = json_data.get("carPlate")
    identity = json_data.get("identity")
    pagesize = json_data.get("pagesize")
    pageIndex = json_data.get("pageIndex")
    timeOrder = json_data.get("timeOrder")
    serial = json_data.get("serial")
    cur = conn.cursor()
    sql = "select * from `违法事件表` where 1=1"

    if from_time != None:
        sql = sql + " and `时间` >= '" + from_time + "'"
    if to_time != None:
        sql = sql + " and `时间` <='" + to_time + "'"
    if partition != None:
        sql = sql + " and `分区` = '" + partition + "'"
    if illegal_nature != None:
        sql = sql + " and `违法性质` like '%%%%%s%%%%'"%illegal_nature
    if states != None:
        sql = sql + " and `处理结果` = '" + str(states) + "'"
    if identity != None:
        sql = sql + " and `身份证` = '" + identity + "'"
    if carPlate != None:
        sql = sql + " and `车牌` = '" + carPlate + "'"
    if serial != None:
        sql = sql + " and `事件编号`='" + serial + "'"
    if timeOrder != None:
        sql = sql + " order by UNIX_TIMESTAMP(`时间`) %s"%timeOrder

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
    sql = "SHOW FIELDS FROM `违法事件表`"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]
    return jsonify({'msg': msg, 'page': page, 'data': {'labels': labels, 'content': content}})


@worker.route('/delete', methods=['POST'])
def delete_record():
    cur = conn.cursor()
    data = request.data
    json_data = json.loads(data)
    serial = json_data.get("serial")
    sql = "delete from `违法事件表` where `事件编号`='" + serial + "'"
    result = cur.execute(sql)
    if result == 1:
        msg = '操作成功'
    else:
        msg = '操作失败'
    return jsonify({'msg': msg})


@worker.route('/add', methods=['POST'])
def add():
    cur = conn.cursor()
    data = request.data
    json_data = json.loads(data)
    illegal_nature = json_data.get("illegal_nature")
    time = json_data.get("time")
    partition = json_data.get("partition")
    street = json_data.get("street")
    address = json_data.get("address")
    point = json_data.get("point")
    record = json_data.get("record")
    identity = json_data.get("identity")
    carPlate = json_data.get("carPlate")
    cur.execute("call NewProc(@num)")
    sql = "select @num"
    cur.execute(sql)
    num = cur.fetchall()
    serial = num[0][0]
    sql1 = "insert into `违法事件表`(`事件编号`,`违法性质`,`时间`,`分区`," \
           "`街道`,`地点`,`坐标`,`违规证明`,`处理结果`,`车牌`,`身份证`) values" \
           "('%s','%s','%s','%s','%s','%s','%s','%s',1,'%s','%s')"%(serial, illegal_nature, time, partition,
                                street, address, point, record, carPlate, identity)
    cur.execute(sql1)
    return jsonify({})


@worker.route("/edit", methods=['POST'])
def edit():
    cur = conn.cursor()
    data = request.data
    json_data = json.loads(data)
    serial = json_data.get("serial")
    illegal_nature = json_data.get("illegal_nature")
    time = json_data.get("time")
    partition = json_data.get("partition")
    street = json_data.get("street")
    address = json_data.get("address")
    identity = json_data.get("identity")
    carPlate = json_data.get("carPlate")
    record = json_data.get("record")
    states = json_data.get("states")

    sql = "UPDATE `违法事件表` SET `事件编号`= %s " % serial
    if time != None:
        sql = sql + ", `时间` = '%s'"%time
    if partition != None:
        sql = sql + " ,`分区` = '" + partition + "'"
    if street != None:
        sql = sql + " ,`街道` = '" + street + "'"
    if address != None:
        sql = sql + " ,`地点` = '" + address + "'"
    if illegal_nature != None:
        sql = sql + " ,`违法性质` = '%s'"%illegal_nature
    if states != None:
        sql = sql + " ,`处理结果` = %s"%states
    if identity != None:
        sql = sql + " ,`身份证` = '" + identity + "'"
    if carPlate != None:
        sql = sql + " ,`车牌` = '" + carPlate + "'"
    if record != None:
        sql = sql + " ,`违规证明` = '" + record + "'"
    sql = sql + " where `事件编号` = %s"%serial
    print(sql)
    result = cur.execute(sql)
    print(result)
    msg = '修改失败'
    if result == 1:
        msg = '修改成功'
    else:
        msg = '修改失败'

    return jsonify({'msg': msg})
