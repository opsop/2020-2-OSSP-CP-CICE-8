from flask import Flask, request, jsonify
import json
import sqlite3
import os
from hotKeyword import *

disasterDBPath = os.path.dirname(__file__) + '/CoronaBotDB/disaster_message_temp.db'
# @app.route('/city_info', methods = ['POST'])

def emergency_alerts(body):
    try:
        hotKeyword("재난문자")
        #print(disasterDBPath)
        print(body)
        conn = sqlite3.connect(disasterDBPath)

        cur = conn.cursor()
        # data = json.loads(body)

        # req = request.get_json()

        li = "%" + "%".join(body["sys_location"].split(" ")) + "%"
        # li = "%"+"%".join(body["city"].split(" "))+"%"


        # 사용자 발화값 예외 처리
        city = li.split("%")
        if city[1] == "세종시":
            city[1] = "세종특별자치시"
            li = "%".join(city)

        elif city[1] == "서울시":
            city[1] == "서울특별시"
            li = "%".join(city)

        elif city[1] == "충북":
            city[1] = "충청북도"
            li = "%".join(city)

        elif city[1] == "충남":
            city[1] = "충청남도"
            li = "%".join(city)

        elif city[1] == "제주도":
            city[1] = "제주특별자치도"
            li = "%".join(city)

        elif city[1] == "경북":
            city[1] = "경상북도"
            li = "%".join(city)

        elif city[1] == "경남":
            city[1] = "경상남도"
            li = "%".join(city)

        elif city[1] == "전북":
            city[1] = "전라북도"
            li = "%".join(city)

        elif city[1] == "전남":
            city[1] = "전라남도"
            li = "%".join(city)

        elif city[1] == "충청도":
            city[1] = "충청"
            li = "%".join(city)

        elif city[1] == "전라도":
            city[1] = "전라"
            li = "%".join(city)

        elif city[1] == "경상도":
            city[1] = "경상"
            li = "%".join(city)

        elif city[1] == "울산시":
            city[1] = "울산광역시"
            li = "%".join(city)

        elif city[1] == "대전시":
            city[1] = "대전광역시"
            li = "%".join(city)

        elif city[1] == "부산시":
            city[1] = "부산광역시"
            li = "%".join(city)

        elif city[1] == "대구시":
            city[1] = "대구광역시"
            li = "%".join(city)

        elif city[1] == "인천시":
            city[1] = "인천광역시"
            li = "%".join(city)

        elif city[1] == "광주시":
            city[1] = "광주광역시"
            li = "%".join(city)

        elif city[1] == "울릉도":
            city[1] = "울릉"
            li = "%".join(city)

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
    finally:
        cur.close()
        conn.close()