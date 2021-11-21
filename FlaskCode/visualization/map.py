from flask import Blueprint
import json
import pymysql
from settings import mysql_connect

map_count = Blueprint('map_count', __name__)

conn = mysql_connect()


@map_count.route('/map_count', methods=['GET'])
def mapping():
    try:
        cur = conn.cursor()
        sql = ''' 
                   select * from hangzhou
                '''
        cur.execute(sql)
        data = cur.fetchall()
        fields = cur.description
        cur.close()
        conn.close()
        jsonData = []
        for i in fields:
            jsonData.append(i[0])
        print(jsonData)
        jsondata1 = []
        jsondata = []
        for row in data:
            result = {}
            new_numbers = []
            for n in row[0].split(','):
                new_numbers.append(float(n))
            result[jsonData[0]] = new_numbers
            result[jsonData[1]] = int(row[1])
            jsondata.append(result)
            print('转换为列表字典的原始数据：', jsondata)
        jsondata1.append(jsondata)
    except:
        print('MySQL connect fail...')
    else:
        jsondatar = json.dumps(jsondata1, ensure_ascii=False)
        # 去除首尾的中括号
        return jsondatar
