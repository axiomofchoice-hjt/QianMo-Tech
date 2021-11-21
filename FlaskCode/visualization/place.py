from flask import Blueprint
import json
import pymysql
from settings import mysql_connect

place = Blueprint('place', __name__)
conn = mysql_connect()


@place.route("/place", methods=['GET'])
def place_count():
    try:
        cur = conn.cursor()
        sql = ''' 
                 SELECT hello.`违法事件表`.`街道` as name,count(*) as value
                 from hello.`违法事件表` 
                 GROUP BY  hello.`违法事件表`.`街道` 
                 ORDER BY COUNT(*) DESC
                 limit 0,20 
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
            result[jsonData[1]] = int(row[1])
            jsondata.append(result)

    except:
        print('MySQL connect fail...')
    else:
        jsondatar = json.dumps(jsondata, ensure_ascii=False)
        return jsondatar
