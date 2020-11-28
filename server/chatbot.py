from flask import Flask, jsonify, request
from KoreaAPIData import KoreaCoronaAPI
from globalData import globalData
from msg_app import emergency_alerts_service
#-*- coding:utf-8 -*-
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
import json
import requests
import re #계산을 위한 특수문자 제거
from naverNews import *
from msg_app.emergency_alerts_service import *

app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
    dataSend = {
      "user" : "corona_chatbot",
      "Subject" : "OSSP",
    }
    return jsonify(dataSend)

@app.route('/city_info', methods=['POST'])
def CityInfo():
    body = json.loads(request.data)
    # req = request.get_json()
    params = body["action"]["params"]
    return emergency_alerts(params)

@app.route('/globalData',methods = ['POST'])
def Global():
    # get request and return json message for global
    dataSend = globalData(request.get_json())
    return jsonify(dataSend)

@app.route('/naver_news', methods=['POST'])
def Naver_news():
    body = request.get_json()
    content = body["action"]["detailParams"]["corona_topic"]["origin"]
    return jsonify(get_current_news(str(content)))

@app.route('/KoreaData',methods = ['GET','POST'])
def KoreaData():
    KoreaResult = KoreaCoronaAPI()
    
    return jsonify(KoreaResult)


@app.route('/city_info', methods=['POST'])
def post():
    body = json.loads(request.data)
    # req = request.get_json()
    params = body["action"]["params"]
    return emergency_alerts_service.emergency_alerts(params)


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
    return kakaoi.simpleText("서버테스트")

if __name__ == "__main__":
    app.run(host='0.0.0.0') # default Flask port : 5000
