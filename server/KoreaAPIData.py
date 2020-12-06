#-*- coding:utf-8 -*-
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
# from . import * #if using on django , should using .apikey instead apikey 
import json 
import requests
import re #계산을 위한 특수문자 제거

from matplotlib import pyplot as plt
from datetime import datetime, date, timedelta # 시각화에서 일주일간 날짜 정보 받아오기 위함
# from KoreaDataDB import create_table, insert_data, select_all, select_updateTime, delete_updateTime, dumpDB #KoreaDB 정의 및 사용 함수들 정의된 파일
from KoreaDataDB import *
import matplotlib.pyplot as plt

# http://192.168.25.30:5000/KoreaData

def KoreaAPI():
    # Corona API에서 API 데이터 받아오기
    #####
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

    print(data)
    data.update(data2)

    return data

# API 데이터를 챗봇 메시지 출력 형식에 맞게 리턴
def KoreaCorona(param='현황 보기'):
    # 국내 코로나 API 데이터 가져오기
    apiData=KoreaAPI()

    # KoreaDataDB의 함수들 사용
    import KoreaDataDB
    KoreaDataDBValues=KoreaDataDB.select_all()
    print("\n", KoreaDataDBValues)
    
    YEAR= datetime.today().year        # 현재 연도 가져오기
    MONTH= datetime.today().month      # 현재 월 가져오기
    DAY= datetime.today().day        # 현재 일 가져오기
    TodayDate=str(YEAR)+"."+str(MONTH)+"."+str(DAY)
    print(TodayDate)
    
    # 오늘자 최신 데이터를 DB에 insert
    KoreaDataDB.insert_data(TodayDate, apiData['TotalCase'], apiData['TotalDeath'], apiData['TotalRecovered'], 
                            apiData['NowCase'], apiData['TotalChecking'], apiData['data0_1'], apiData['TodayRecovered'])


    # 국내 현황 메시지
    print("\n", KoreaDataDB.select_all())
    # DB 데이터 정렬을 통해, DB 데이터 중에 최신 데이터 출력
    totalValue=list(KoreaDataDB.select_all())
    totalValue.sort(reverse=True) 
    print(totalValue)
    # 오늘자 데이터가 아직 DB에 없을 경우를 대비해서, DB의 데이터 중 가장 최신 데이터를 반환할 수 있도록 함. (에러 방지)
    currentValue=totalValue[0]

    messages="""국내 코로나 현황입니다.
(%s 기준)
확진자 %s명 (+%s)
완치자 %s명 (+%s)
사망자 %s명 
격리자 %s명 """ %(currentValue[0], currentValue[1], currentValue[6],currentValue[7], # currentValue['updateTime'], currentValue['TotalCase'], currentValue['TodayCase'],currentValue['TotalRecovered'],
    currentValue[3], currentValue[2], currentValue[4]) # currentValue['TodayRecovered'], currentValue['TotalDeath'], currentValue['NowCase']
    print(messages)

    # 되묻기 질문에 대한 응답. 
    if param == "현황 보기":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [                  
                    {
                        "simpleText":{
                            "text" : messages
                        }
                    }
                ]
            }
        }
    elif param == "추이 그래프":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": "확진자 추이 그래프",
                            "description": "일주일 간 국내 확진자 추이 현황",
                            "thumbnail": {
                                "imageUrl": "https://i.esdrop.com/d/KVTpYYElDK.png" # 직접 만든 시각화 이미지의 URL
                            },
                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "바로가기",
                                "webLinkUrl": "http://ncov.mohw.go.kr/"
                            }          
                        ]
                        }
                    }
                ]  
            }
        }
    else: # 현황보기/ 추이 그래프가 입력되지 않은 경우.
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [ # 봇 테스트로 확인하기                 
                    {
                        "simpleText":{
                            "text" : "다시 입력해주세요."
                        }
                    }
                ]
            }
        }

    return dataSend

'''
def visualizeKoreaPlot():
    # 국내 데이터 꺾은선 시각화

    # KoreaDB에 당일 데이터 저장
    apiData=KoreaAPI()
    YEAR= datetime.today().year

    KoreaDataDBValues=KoreaDataDB.select_all()
    print("\n", KoreaDataDBValues)
    
    YEAR= datetime.today().year        # 현재 연도 가져오기
    MONTH= datetime.today().month      # 현재 월 가져오기
    DAY= datetime.today().day        # 현재 일 가져오기
    TodayDate=str(YEAR)+"."+str(MONTH)+"."+str(DAY)
    print(TodayDate)
    
    # if KoreaDataDBValues[-1][0] !=TodayDate 일때만 한다.
    KoreaDataDB.insert_data(str(YEAR)+"."+apiData['updateTime'][23:28], apiData['TotalCase'], apiData['TotalDeath'], apiData['TotalRecovered'], 
                            apiData['NowCase'], apiData['TotalChecking'], apiData['data0_1'], apiData['TodayRecovered'])

'''                            