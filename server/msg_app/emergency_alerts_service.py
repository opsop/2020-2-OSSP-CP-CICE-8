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

# @app.route('/city_info', methods = ['POST'])
def emergency_alerts(body):
    conn = sqlite3.connect('CSID-DGU/2020-2-OSSP-CP-CICE-8/server/msg_app/disaster_message_temp.db')
    cur = conn.cursor()
    # data = json.loads(body)
    # req = request.get_json()

    li = "%" + "%".join(body["sys_location"].split(" ")) + "%"
    # li = "%"+"%".join(body["city"].split(" "))+"%"

    # SQL 쿼리 실행
    cur.execute("select * from MESSAGE where location_name like '" + li + "'")
    # 데이터 Fetch
    rows = cur.fetchall()
    msg_list = []
    for row in rows:
        msg_list.append(row)
    # for row in rows:
    #   print(row)
    if len(msg_list) > 3:
        msg_list = msg_list[0:3]
        print(msg_list[0][0])

    elif len(msg_list) == 0:
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "해당지역에는 최근에 온 재난문자가 없습니다."
                        }
                    }
                ]
            }
        }

        return jsonify(res)

    msg_li = []

    for i in range(0, len(msg_list)):
        msg_list[i] = msg_list[i][1:]
        for j in range(0, len(msg_list[0])):
            print(msg_list[i])
            msg_tmp = "\n".join(msg_list[i])
        msg_li.append(msg_tmp)

    msg = "\n\n".join(msg_li)

    default_msg = "[재난문자를 최신순으로 최대 3개까지 표시]"
    tmp = []
    tmp.append(default_msg)
    tmp.append(msg)
    msg = "\n".join(tmp)

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": msg
                    }
                }
            ]
        }
    }

    return jsonify(res)

    conn.close()