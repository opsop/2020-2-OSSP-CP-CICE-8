from flask import Flask, jsonify, request

#-*- coding:utf-8 -*-
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
import json
import requests
import re #계산을 위한 특수문자 제거

SECURE_SSL_REDIRECT = False

# 스케줄링에 필요한 모듈
from apscheduler.schedulers.background import BackgroundScheduler

# 카카오 챗봇 기능별 메소드
from KoreaAPIData import KoreaCoronaAPI, visualizeKoreaPlot # 국내 현황, 국내 확진자 추이 시각화
from globalData import globalData # 전세계 데이터
from msg_app import emergency_alerts_service # 재난문자
from emergency_service import * # 재난문자
from hospital_pharmacy import hospital_info # 병원/약국 정보
from triage_center import triage # 선별 진료소
from hotKeyword import * # 인기 키워드
from naverNews import naver_get # 네이버 뉴스
#from youtubeNews import youtubeNews # 유투브 뉴스
from youtube import tube_get # 유튜브 뉴스
from self_diagnosis import * # 자가진단
from distance_level import * # 사회적 거리두기


# db 업데이트
def update_db():
    print("db 업데이트 진행중")
    import disaster_msg
    # 업데이트할 것들 여기에

sched = BackgroundScheduler(daemon=True)
sched.add_job(update_db, 'interval', hours=24)
sched.start()


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
    dataSend = naver_get(content)
    return jsonify(dataSend)

# 유튜브 뉴스 -나영 -이걸로 작동!
@app.route('/Youtube', methods=['POST'])
def Youtube():
    body = request.get_json()
    content = body["action"]["detailParams"]["youtube_corona"]["origin"]
    dataSend = tube_get(content)
    return jsonify(dataSend)

# 유투브 뉴스 -승민 -아직 미작동(테스트용)
@app.route('/youtube_news', methods=['POST'])
def Youtube_news():
    body = request.get_json()
    
    return jsonify(output)

# 국내 코로나 현황
@app.route('/KoreaData',methods = ['GET','POST'])
def KoreaData():
    body = request.get_json() # 되묻기 질문용도
    KoreaResult = KoreaCoronaAPI() 
    hotKeyword("국내현황")
    return jsonify(KoreaResult)


# 선별진료소 안내
@app.route('/triagecenter_info', methods=['POST'])
def Triage():
    body = request.get_json()
    return jsonify(triage(body))


# 병원및약국 안내
@app.route('/hospital_info', methods=['POST'])
def Hospital():
    body = request.get_json()
    return jsonify(hospital_info(body))

# 인기 키워드 검색기능
@app.route('/hotKeyword' , methods = ['POST'])
def HotKeyword():
    body = request.get_json()
    return jsonify(searchHotKeyword(body))

# 자가진단 테스트
@app.route('/self_diagnosis', methods = ['POST'])
def Diagnosis():
    body = json.loads(request.data)
    return jsonify(self_diagnosis(body))

# 사회적 거리두기
@app.route('/distance_level', methods = ['POST'])
def Distance():
    body = json.loads(request.data)
    return jsonify(distance_level(body))


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
