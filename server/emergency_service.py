from flask import Flask, request, jsonify
import json
import sqlite3
import os
from hotKeyword import *

disasterDBPath = os.path.dirname(__file__) + '/CoronaBotDB/disaster_message_temp.db'
max = 3 # 최대로 나타낼 재난 문자 개수


def emergency_alerts(body):
    try:
        hotKeyword("재난 문자 현황") # 인기 키워드 DB에 넣기

        conn = sqlite3.connect(disasterDBPath)

        cur = conn.cursor()

        entity_first = body["sys_location"]
        entity_second = body["sys_location1"]

        # 사용자 발화 값에 대한 예외 처리 부분
        if entity_first == entity_second:  # 도 / 광역시 에 대해 전체를 알고 싶은 경우 (예를 들어 서울, 서울이라고 입력했을 때)
            entity_second = "전체"

        elif entity_first == "세종시":
            entity_first = "세종특별자치시"
            entity_second = "전체"

        elif entity_first == "서울시":
            entity_first = "서울특별시"

        elif entity_first == "충북":
            entity_first = "충청북도"

        elif entity_first == "충남":
            entity_first = "충청남도"

        elif entity_first == "제주도":
            entity_first = "제주특별자치도"
            entity_second = "전체"

        elif entity_first == "경북":
            entity_first = "경상북도"

        elif entity_first == "경남":
            entity_first = "경상남도"

        elif entity_first == "전북":
            entity_first = "전라북도"

        elif entity_first == "전남":
            entity_first = "전라남도"

        elif entity_first == "충청도":
            entity_first = "충청"

        elif entity_first == "전라도":
            entity_first = "전라"

        elif entity_first == "경상도":
            entity_first = "경상"

        elif entity_first == "울산시":
            entity_first = "울산광역시"

        elif entity_first == "대전시":
            entity_first = "대전광역시"

        elif entity_first == "부산시":
            entity_first = "부산광역시"

        elif entity_first == "대구시":
            entity_first = "대구광역시"

        elif entity_first == "인천시":
            entity_first = "인천광역시"

        elif entity_first == "광주시":
            entity_first = "광주광역시"

        elif entity_first == "울릉도":
            entity_first = "울릉"

        elif entity_second == "세종시":
            entity_second = "세종특별자치시"
            entity_first = "전체"

        elif entity_second == "서울시":
            entity_second = "서울특별시"

        elif entity_second == "충북":
            entity_second = "충청북도"

        elif entity_second == "충남":
            entity_second = "충청남도"

        elif entity_second == "제주도":
            entity_second = "제주특별자치도"
            entity_first = "전체"

        elif entity_second == "경북":
            entity_second = "경상북도"

        elif entity_second == "경남":
            entity_second = "경상남도"

        elif entity_second == "전북":
            entity_second = "전라북도"

        elif entity_second == "전남":
            entity_second = "전라남도"

        elif entity_second == "충청도":
            entity_second = "충청"

        elif entity_second == "전라도":
            entity_second = "전라"

        elif entity_second == "경상도":
            entity_second = "경상"

        elif entity_second == "울산시":
            entity_second = "울산광역시"

        elif entity_second == "대전시":
            entity_second = "대전광역시"

        elif entity_second == "부산시":
            entity_second = "부산광역시"

        elif entity_second == "대구시":
            entity_second = "대구광역시"

        elif entity_second == "인천시":
            entity_second = "인천광역시"

        elif entity_second == "광주시":
            entity_second = "광주광역시"

        elif entity_second == "울릉도":
            entity_second = "울릉"

        if entity_second == "전체":
            li = "%" + entity_first + "%"

        elif entity_first == "전체":
            li = "%" + entity_second + "%"

        else:
            li = "%" + entity_first + "%" + entity_second + "%"

        # SQL 쿼리 실행
        cur.execute("select * from MESSAGE where location_name like '" + li + "'")
        # 데이터 Fetch
        rows = cur.fetchall()
        msg_list = []
        for row in rows:
            msg_list.append(row)
        # for row in rows:
        #   print(row)
        if len(msg_list) > max:  # 해당 지역에 최근에 온 재난 문자가 max인 3개보다 많을 때
            msg_list = msg_list[0:max]

        elif len(msg_list) == 0:  # 해당 지역에 최근에 온 재난 문자가 없을 때
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
            msg_list[i] = msg_list[i][1:]  # 첫번째 재난 문자(msg_list[i][0]) 이후로 온 재난 문자를 표시할 때 한 줄씩 띄어서 쓰기 위해
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
