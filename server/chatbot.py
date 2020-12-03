from flask import Flask, jsonify, request
from KoreaAPIData import KoreaCoronaAPI, visualizeKoreaPlot
from globalData import globalData
from msg_app import emergency_alerts_service
#-*- coding:utf-8 -*-
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
import json
import requests
import re #계산을 위한 특수문자 제거

SECURE_SSL_REDIRECT = False

# 카카오 챗봇 기능별 메소드
from naverNews import *
from msg_app.emergency_alerts_service import *
from hospital_pharmacy import hospital_info
from triage_center import triage
from hotKeyword import *

app = Flask(__name__)

# api Test
@app.route('/keyboard')
def Keyboard():
    dataSend = {
      "user" : "corona_chatbot",
      "Subject" : "OSSP",
    }
    return jsonify(dataSend)

# 긴급 재난문자
@app.route('/city_info', methods=['POST'])
def CityInfo():
    body = json.loads(request.data)
    print(body)
    # req = request.get_json()
    params = body["action"]["params"]
    return emergency_alerts(params)

# 전세계 현황 데이터
@app.route('/globalData',methods = ['POST'])
def Global():
    # get request and return json message for global
    dataSend = globalData(request.get_json())
    return jsonify(dataSend)

# 네이버 뉴스
@app.route('/naver_news', methods=['POST'])
def Naver_news():
    body = request.get_json()
    content = body["action"]["detailParams"]["corona_topic"]["origin"]
    output = get_current_news(content)
    print(output)
    exoutput = exc()
    if content == "기타 검색":
        return jsonify(exoutput)
    else :
        return jsonify(output)

# 유튜브 뉴스
@app.route('/Youtube', methods=['POST'])
def Youtube():
    body = request.get_json()
    dataSend = you_news(body)
    print(dataSend)
    return jsonify(dataSend)

# 국내 코로나 현황
@app.route('/KoreaData',methods = ['GET','POST'])
def KoreaData():
    KoreaResult = KoreaCoronaAPI()
    visualizeKoreaPlot()
    return jsonify(KoreaResult)

@app.route('/triagecenter_info', methods=['POST'])
def Triage():
    body = request.get_json()
    return jsonify(triage(body))

@app.route('/hospital_info', methods=['POST'])
def Hospital():
    body = request.get_json()
    return jsonify(hospital_info(body))

# 인기 키워드 검색기능
@app.route('/hotKeyword' , methods = ['POST'])
def HotKeyword():
    body = request.get_json()
    return jsonify(searchHotKeyword(body))

# 서버 테스트 ( 카카오 오픈빌더 return format )
@app.route('/message', methods=['POST'])
def Message():
    content = request.get_json()
    print(content)
    content = content['userRequest']
    content = content['utterance']

    if content.rstrip() == "안녕":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : "서버테스트"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    else :
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "질문을 이해하지 못했습니다."
                        }
                    }
                ]
            }
        }
    return dataSend

if __name__ == "__main__":
    app.run(host='0.0.0.0') # default Flask port : 5000
