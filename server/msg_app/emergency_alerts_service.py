from flask import Flask, request, jsonify
#import json
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
    #li = "%"+"%".join(body["city"].split(" "))+"%"
    li = "%" + "%".join(body["sys_location"].split(" ")) + "%"


    # SQL 쿼리 실행
    cur.execute("select * from MESSAGE where location_name like '" + li+"'")
    # 데이터 Fetch
    rows = cur.fetchall()
    msg_list = []
    for row in rows:
        msg_list.append(row)
    #for row in rows:
     #   print(row)
    d = {"msg_list" : msg_list}
    return jsonify(d)

    conn.close()