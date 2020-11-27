from flask import Flask, request, jsonify
import json
import sqlite3

# try:
#     conn.close()
# except:
#     print(0000000)
#     pass
# SQLite DB 연결

# Connection 으로부터 Cursor 생성


def emergency_alerts(body):
    conn = sqlite3.connect("disaster_message_temp.db")
    cur = conn.cursor()

    li = "%"+"%".join(body["sys_location"].split(" "))+"%"
    #li = "%"+"%".join(body["city"].split(" "))+"%"


    # SQL 쿼리 실행
    cur.execute("select * from MESSAGE where location_name like '" + li+"'")
    # 데이터 Fetch
    rows = cur.fetchall()
    msg_list = []
    for row in rows:
        msg_list.append(row)
    #for row in rows:
     #   print(row)
    #res = {"msg_list" : msg_list}
    if len(msg_list)>3:
        msg_list = msg_list[0:3]
    elif len(msg_list)==0:
        res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "최근에 온 재난문자가 없습니다."
                    }
                }
            ]
        }
    }
        return jsonify(res)
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": msg_list
                    }
                }
            ]
        }
    }
    return jsonify(res)

    conn.close()