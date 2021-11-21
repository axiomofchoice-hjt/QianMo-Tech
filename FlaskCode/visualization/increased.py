from flask import Blueprint, jsonify
from settings import mysql_connect

increased = Blueprint('increased', __name__)
conn = mysql_connect()


@increased.route("/increased", methods=['GET'])
def increase():
    cur = conn.cursor()
    sql = "select DATE_FORMAT(`时间`, '%m/%d') From increased_3_4"
    cur.execute(sql)
    data = cur.fetchall()
    jsonData = []
    for i in data:
        jsonData.append(i[0])

    sql11 = "select `事件数目` From increased_1_1"
    cur.execute(sql11)
    data = cur.fetchall()
    jsonData11 = []
    for i in data:
        jsonData11.append(i[0])

    sql12 = "select `事件数目` From increased_1_2"
    cur.execute(sql12)
    data = cur.fetchall()
    jsonData12 = []
    for i in data:
        jsonData12.append(i[0])

    sql13 = "select `事件数目` From increased_1_3"
    cur.execute(sql13)
    data = cur.fetchall()
    jsonData13 = []
    for i in data:
        jsonData13.append(i[0])

    sql14 = "select `事件数目` From increased_1_4"
    cur.execute(sql14)
    data = cur.fetchall()
    jsonData14 = []
    for i in data:
        jsonData14.append(i[0])

    sql15 = "select `事件数目` From increased_1_5"
    cur.execute(sql15)
    data = cur.fetchall()
    jsonData15 = []
    for i in data:
        jsonData15.append(i[0])

    sql16 = "select `事件数目` From increased_1_6"
    cur.execute(sql16)
    data = cur.fetchall()
    jsonData16 = []
    for i in data:
        jsonData16.append(i[0])

    sql17 = "select `事件数目` From increased_1_7"
    cur.execute(sql17)
    data = cur.fetchall()
    jsonData17 = []
    for i in data:
        jsonData17.append(i[0])

    sql18 = "select `事件数目` From increased_1_8"
    cur.execute(sql18)
    data = cur.fetchall()
    jsonData18 = []
    for i in data:
        jsonData18.append(i[0])

    sql19 = "select `事件数目` From increased_1_9"
    cur.execute(sql19)
    data = cur.fetchall()
    jsonData19 = []
    for i in data:
        jsonData19.append(i[0])

    sql110 = "select `事件数目` From increased_1_10"
    cur.execute(sql110)
    data = cur.fetchall()
    jsonData110 = []
    for i in data:
        jsonData110.append(i[0])

    sql111 = "select `事件数目` From increased_1_11"
    cur.execute(sql111)
    data = cur.fetchall()
    jsonData111 = []
    for i in data:
        jsonData111.append(i[0])

    sql112 = "select `事件数目` From increased_1_12"
    cur.execute(sql112)
    data = cur.fetchall()
    jsonData112 = []
    for i in data:
        jsonData112.append(i[0])

    sql113 = "select `事件数目` From increased_1_13"
    cur.execute(sql113)
    data = cur.fetchall()
    jsonData113 = []
    for i in data:
        jsonData113.append(i[0])

    sql21 = "select `事件数目` From increased_2_1"
    cur.execute(sql21)
    data = cur.fetchall()
    jsonData21 = []
    for i in data:
        jsonData21.append(i[0])

    sql22 = "select `事件数目` From increased_2_2"
    cur.execute(sql22)
    data = cur.fetchall()
    jsonData22 = []
    for i in data:
        jsonData22.append(i[0])

    sql23 = "select `事件数目` From increased_2_3"
    cur.execute(sql23)
    data = cur.fetchall()
    jsonData23 = []
    for i in data:
        jsonData23.append(i[0])

    sql24 = "select `事件数目` From increased_2_4"
    cur.execute(sql24)
    data = cur.fetchall()
    jsonData24 = []
    for i in data:
        jsonData24.append(i[0])

    sql25 = "select `事件数目` From increased_2_5"
    cur.execute(sql25)
    data = cur.fetchall()
    jsonData25 = []
    for i in data:
        jsonData25.append(i[0])

    sql26 = "select `事件数目` From increased_2_6"
    cur.execute(sql26)
    data = cur.fetchall()
    jsonData26 = []
    for i in data:
        jsonData26.append(i[0])

    sql27 = "select `事件数目` From increased_2_7"
    cur.execute(sql27)
    data = cur.fetchall()
    jsonData27 = []
    for i in data:
        jsonData27.append(i[0])

    sql28 = "select `事件数目` From increased_2_8"
    cur.execute(sql28)
    data = cur.fetchall()
    jsonData28 = []
    for i in data:
        jsonData28.append(i[0])

    sql29 = "select `事件数目` From increased_2_9"
    cur.execute(sql29)
    data = cur.fetchall()
    jsonData29 = []
    for i in data:
        jsonData29.append(i[0])

    sql210 = "select `事件数目` From increased_2_10"
    cur.execute(sql210)
    data = cur.fetchall()
    jsonData210 = []
    for i in data:
        jsonData210.append(i[0])

    sql211 = "select `事件数目` From increased_2_11"
    cur.execute(sql211)
    data = cur.fetchall()
    jsonData211 = []
    for i in data:
        jsonData211.append(i[0])

    sql212 = "select `事件数目` From increased_2_12"
    cur.execute(sql212)
    data = cur.fetchall()
    jsonData212 = []
    for i in data:
        jsonData212.append(i[0])

    sql213 = "select `事件数目` From increased_2_13"
    cur.execute(sql213)
    data = cur.fetchall()
    jsonData213 = []
    for i in data:
        jsonData213.append(i[0])

    sql31 = "select `事件数目` From increased_3_1"
    cur.execute(sql31)
    data = cur.fetchall()
    jsonData31 = []
    for i in data:
        jsonData31.append(i[0])

    sql32 = "select `事件数目` From increased_3_2"
    cur.execute(sql32)
    data = cur.fetchall()
    jsonData32 = []
    for i in data:
        jsonData32.append(i[0])

    sql33 = "select `事件数目` From increased_3_3"
    cur.execute(sql33)
    data = cur.fetchall()
    jsonData33 = []
    for i in data:
        jsonData33.append(i[0])

    sql34 = "select `事件数目` From increased_3_4"
    cur.execute(sql34)
    data = cur.fetchall()
    jsonData34 = []
    for i in data:
        jsonData34.append(i[0])

    sql35 = "select `事件数目` From increased_3_5"
    cur.execute(sql35)
    data = cur.fetchall()
    jsonData35 = []
    for i in data:
        jsonData35.append(i[0])

    sql36 = "select `事件数目` From increased_3_6"
    cur.execute(sql36)
    data = cur.fetchall()
    jsonData36 = []
    for i in data:
        jsonData36.append(i[0])

    sql37 = "select `事件数目` From increased_3_7"
    cur.execute(sql37)
    data = cur.fetchall()
    jsonData37 = []
    for i in data:
        jsonData37.append(i[0])

    sql38 = "select `事件数目` From increased_3_8"
    cur.execute(sql38)
    data = cur.fetchall()
    jsonData38 = []
    for i in data:
        jsonData38.append(i[0])

    sql39 = "select `事件数目` From increased_3_9"
    cur.execute(sql39)
    data = cur.fetchall()
    jsonData39 = []
    for i in data:
        jsonData39.append(i[0])

    sql310 = "select `事件数目` From increased_3_10"
    cur.execute(sql310)
    data = cur.fetchall()
    jsonData310 = []
    for i in data:
        jsonData310.append(i[0])

    sql311 = "select `事件数目` From increased_3_11"
    cur.execute(sql311)
    data = cur.fetchall()
    jsonData311 = []
    for i in data:
        jsonData311.append(i[0])

    sql312 = "select `事件数目` From increased_3_12"
    cur.execute(sql312)
    data = cur.fetchall()
    jsonData312 = []
    for i in data:
        jsonData312.append(i[0])

    sql313 = "select `事件数目` From increased_3_13"
    cur.execute(sql313)
    data = cur.fetchall()
    jsonData313 = []
    for i in data:
        jsonData313.append(i[0])
    return jsonify({"type": [{"key": "helmet", "text": "未佩戴头盔事件发生的趋势"},
                             {"key": "red", "text": "闯红灯事件发生的趋势"},
                             {"key": "direction", "text": "逆行事件发生的趋势"}],
                    "common": {
                        "day": jsonData
                    },
                    "helmet": {
                        "title": "未佩戴头盔时间发生的趋势",
                        "data": [
                            {
                                "name": "上城区",
                                "data": jsonData31
                            },
                            {
                                "name": "拱墅区",
                                "data": jsonData32
                            },
                            {
                                "name": "西湖区",
                                "data": jsonData33
                            },
                            {
                                "name": "滨江区",
                                "data": jsonData34
                            },
                            {
                                "name": "萧山区",
                                "data": jsonData35
                            },
                            {
                                "name": "余杭区",
                                "data": jsonData36
                            },
                            {
                                "name": "临平区",
                                "data": jsonData37
                            },
                            {
                                "name": "钱塘区",
                                "data": jsonData38
                            },
                            {
                                "name": "富阳区",
                                "data": jsonData39
                            },
                            {
                                "name": "临安区",
                                "data": jsonData310
                            },
                            {
                                "name": "桐庐县",
                                "data": jsonData311
                            },
                            {
                                "name": "淳安县",
                                "data": jsonData312
                            },
                            {
                                "name": "建德市",
                                "data": jsonData313
                            }
                        ]

                    },
                    "red": {
                        "title": "闯红灯事件发生的趋势",
                        "data": [
                            {
                                "name": "上城区",
                                "data": jsonData11
                            },
                            {
                                "name": "拱墅区",
                                "data": jsonData12
                            },
                            {
                                "name": "西湖区",
                                "data": jsonData13
                            },
                            {
                                "name": "滨江区",
                                "data": jsonData14
                            },
                            {
                                "name": "萧山区",
                                "data": jsonData15
                            },
                            {
                                "name": "余杭区",
                                "data": jsonData16
                            },
                            {
                                "name": "临平区",
                                "data": jsonData17
                            },
                            {
                                "name": "钱塘区",
                                "data": jsonData18
                            },
                            {
                                "name": "富阳区",
                                "data": jsonData19
                            },
                            {
                                "name": "临安区",
                                "data": jsonData110
                            },
                            {
                                "name": "桐庐县",
                                "data": jsonData111
                            },
                            {
                                "name": "淳安县",
                                "data": jsonData112
                            },
                            {
                                "name": "建德市",
                                "data": jsonData113
                            }

                        ]
                    },
                    "direction": {
                        "title": "逆行事件发生的趋势",
                        "data": [
                            {
                                "name": "上城区",
                                "data": jsonData21
                            },
                            {
                                "name": "拱墅区",
                                "data": jsonData22
                            },
                            {
                                "name": "西湖区",
                                "data": jsonData23
                            },
                            {
                                "name": "滨江区",
                                "data": jsonData24
                            },
                            {
                                "name": "萧山区",
                                "data": jsonData25
                            },
                            {
                                "name": "余杭区",
                                "data": jsonData26
                            },
                            {
                                "name": "临平区",
                                "data": jsonData27
                            },
                            {
                                "name": "钱塘区",
                                "data": jsonData28
                            },
                            {
                                "name": "富阳区",
                                "data": jsonData29
                            },
                            {
                                "name": "临安区",
                                "data": jsonData210
                            },
                            {
                                "name": "桐庐县",
                                "data": jsonData211
                            },
                            {
                                "name": "淳安县",
                                "data": jsonData212
                            },
                            {
                                "name": "建德市",
                                "data": jsonData213
                            }
                        ]
                    }

                    })
