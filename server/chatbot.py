from flask import Flask, jsonify, request
from globalData import globalData
# from .KoreaAPIData import KoreaCoronaAPI

#-*- coding:utf-8 -*-
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
import json

import requests
import re #계산을 위한 특수문자 제거
from naverNews import *
from msg_app import *

app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
    dataSend = {
      "user" : "corona_chatbot",
      "Subject" : "OSSP",
    }
    return jsonify(dataSend)

@app.route('/city_info')
def CityInfo():
    body = json.loads(request.data)
    # req = request.get_json()
    params = body["action"]["params"]
    return emergency_alerts_service.emergency_alerts(params)

@app.route('/globalData',methods = ['POST'])
def Global():
    # get request and return json message for global
    dataSend = globalData(request.get_json())
    return jsonify(dataSend)

@app.route('/naver_news', methods=['POST'])
def Naver_news():
    body = request.get_json()
    content = body["action"]["detailParams"]["corona_topic"]["value"]
    get_current_news(str(content))
    send = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                {"buttons": [
                                    {
                                        "action": "webLink",
                                        "label": News.news_list[0].title,
                                        "webLinkUrl": News.news_list[0].link
                                    }]},
                                {"buttons": [
                                    {
                                        "action": "webLink",
                                        "label": News.news_list[1].title,
                                        "webLinkUrl": News.news_list[1].link
                                    }]},
                                {"buttons": [
                                    {
                                        "action": "webLink",
                                        "label": News.news_list[2].title,
                                        "webLinkUrl": News.news_list[2].link
                                    }]},
                                {"buttons": [
                                    {
                                        "action": "webLink",
                                        "label": News.news_list[3].title,
                                        "webLinkUrl": News.news_list[3].link
                                    }]},
                                {"buttons": [
                                    {
                                        "action": "webLink",
                                        "label": News.news_list[4].title,
                                        "webLinkUrl": News.news_list[4].link
                                    }]}
                    }]
                }}
        ]
    }
    }
    return jsonify(send)

@app.route('/KoreaData',methods = ['GET','POST'])
def KoreaData():
    # KoreaResult = KoreaCoronaAPI()

    korea = "http://api.corona-19.kr/korea?serviceKey="
    country = "http://api.corona-19.kr/korea/country?serviceKey="

    key = 'f14954c4a0b04d9a53b1603e20d40e1b8' #API 키(https://api.corona-19.kr/ 에서 무료 발급 가능)
    ###
    print('서버에 데이터를 요청하고 있습니다.. \n\n')

    response = requests.get(korea + key)
    text = response.text
    data = json.loads(text)

    response2 = requests.get(country + key)
    text2 = response2.text
    data2 = json.loads(text2)

    #####
    code = response.status_code
    code2 = response2.status_code

    #print(data)
    data.update(data2)
    # dataSend =data

    #for key, value in data.items():  # 인코딩 해결!!
    #    print(valude.decode('utf-8'))


    dataSend={
        "TotalCase":data['TotalCase'],
        "TodayRecovered": data['TodayRecovered'],
        "TotalDeath": data['TotalDeath'],
    }

    return jsonify(dataSend)
    #return KoreaResult

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
