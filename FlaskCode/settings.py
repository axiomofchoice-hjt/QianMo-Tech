import pymysql


def mysql_connect():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='shit',
        db='hello',
        charset='utf8',
        autocommit=True
    )
    return conn
