import json
import traceback

import pymysql
from settings import mysql_connect
from flask import Flask, render_template, request, Blueprint, jsonify, redirect

loginModule = Blueprint('loginModule', __name__)
conn = mysql_connect()


# 获取登录参数及处理
@loginModule.route('/login', methods=['POST'])
def getLoginRequest():
    cur = conn.cursor()
    data = request.data
    json_data = json.loads(data)
    # SQL 查询语句
    sql = "select * from `用户登录表` where `账号`= '%s' and `密码`= '%s' and `身份`= %d"\
          %(json_data.get('username'), json_data.get('password'), json_data.get('class'))
    print(sql)
    try:
        # 执行sql语句
        cur.execute(sql)
        results = cur.fetchall()
        print(len(results))
        if len(results) == 1:
            return jsonify({'msg': '登录成功'})
        else:
            return jsonify({'msg': '用户名或密码不正确'})
        conn.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        conn.rollback()
    # 关闭数据库连接
    conn.close()


@loginModule.route('/register', methods=['POST'])
def register():
    cur = conn.cursor()
    data = request.data
    json_data = json.loads(data)
    class1 = json_data.get("class")
    username = json_data.get("username")
    password = json_data.get("password")
    name = json_data.get("name")
    identity = json_data.get("identity")
    sex = json_data.get("sex")
    phone = json_data.get("phone")
    address = json_data.get("address")
    sql = "INSERT INTO `用户信息表`(`账号`, `姓名`, `身份证`, `性别`, `手机号`, `家庭住址`)" \
          " VALUES ('%s', '%s', '%s', %s, '%s', '%s')" %(username, name, identity, sex,
                                                         phone, address)
    try:
        cur.execute(sql)
        sql1 = "insert into `用户登录表`(`账号`, `密码`, `身份`) values('%s', '%s', %s)" \
               %(username, password, class1)
        cur.execute(sql1)

        return redirect(request.referrer)
    except:
        traceback.print_exc()
        conn.rollback()
        return jsonify({'msg': '注册失败'})
    conn.close()