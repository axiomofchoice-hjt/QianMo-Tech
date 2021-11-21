import json
from flask import Blueprint, render_template, request
import pymysql
from settings import mysql_connect

time_count = Blueprint('time_count', __name__)
conn = mysql_connect()


@time_count.route('/time', methods=['GET'])
def time():
    try:
        cur = conn.cursor()
        sql = ''' 
              select cast(@xuhao:=@xuhao+1 as char) as 'index', a.* from  time1 a, (SELECT @xuhao:=0) b;
        '''
        cur.execute(sql)
        data = cur.fetchall()
        fields = cur.description
        cur.close()
        conn.close()
        jsonData = []
        for i in fields:
            jsonData.append(i[0])
        jsondata = []
        for row in data:
            result = {}
            result[jsonData[0]] = row[0]
            result[jsonData[1]] = row[1]
            result[jsonData[2]] = str(row[2])
            jsondata.append(result)

    except:
        print('MySQL connect fail...')
    else:
        jsondatar = json.dumps(jsondata, ensure_ascii=False)
        # 去除首尾的中括号
        return jsondatar
