from flask import Blueprint
import json
import pymysql
from settings import mysql_connect

today_Count = Blueprint('today_Count', __name__)
conn = mysql_connect()


@today_Count.route('/today', methods=['GET'])
def today_count():
    try:
        cur = conn.cursor()
        sql = ''' 
             SELECT count(*) 
             FROM hello.`违法事件表`
             WHERE TO_DAYS(hello.`违法事件表`.`时间`)=TO_DAYS(NOW())
                 '''
        cur.execute(sql)
        data = cur.fetchall()
        fields = cur.description
        cur.close()
        conn.close()

        jsondata = []
        for row in data:
            result = {}
            result['value'] = int(row[0])
            jsondata.append(result)

    except:
        print('MySQL connect fail...')
    else:
        jsondatar = json.dumps(jsondata, ensure_ascii=False)
        # 去除首尾的中括号
        return jsondatar
