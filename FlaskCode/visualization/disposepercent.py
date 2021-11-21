from flask import Blueprint
import json
import pymysql
from settings import mysql_connect

dispose_percent = Blueprint('dispose_percent', __name__)
conn = mysql_connect()


@dispose_percent.route("/dispose_percent", methods=['GET'])
def dispose():
    try:
        cur = conn.cursor()
        sql = ''' 
                  select  * from disposepercent
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
        jsondata = []
        for row in data:
            result = {}
            result[jsonData[0]] = row[0]
            result[jsonData[1]] = int(row[1])
            result[jsonData[2]] = int(row[2])
            jsondata.append(result)

    except:
        print('MySQL connect fail...')
    else:
        jsondatar = json.dumps(jsondata, ensure_ascii=False)
        # 去除首尾的中括号
        return jsondatar
