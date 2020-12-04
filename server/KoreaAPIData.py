 h#-*- coding:utf-8 -*-
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
# from . import * #if using on django , should using .apikey instead apikey 
import json 
import requests
import re #계산을 위한 특수문자 제거

import KoreaDataDB #KoreaDB 정의 및 사용 함수들 정의된 파일
from matplotlib import pyplot as plt
from datetime import datetime

# http://192.168.25.10:5000/KoreaData

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

def KoreaCoronaAPI():
    # API 데이터를 챗봇 메시지 출력 형식에 맞게 리턴
    data=KoreaAPI()

    messages="""국내 현황
확진자 %s명
완치자 %s명
사망자 %s명
    """ %(data['TotalCase'], data['TotalRecovered'], data['TotalDeath'])
    print(messages)
    dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [ # 봇 테스트로 확인하기                 
                    {
                        "simpleText":{
                            "text" : messages
                        }
                    }
                ]
            }
        }
    # visualizeKoreaPlot()
    return dataSend


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
    
    # 잘못 들어간 DB 데이터 지우거나, 고치기

    # 오늘 포함 7일 데이터 불러와서 시각화
    # TodayCase 바꿔서 출력
    x_values = [0, 1, 2, 3, 4] # for문으로 오늘부터 7일 날짜
    y_values = [0, 1, 4, 9, 16] # for문으로 오늘부터 7일 TodayCase불러오기

    plt.plot(x_values, y_values, color='red',  marker='o')

    plt.ylabel('확진자 증가 추이')
    plt.title('일주일 간 국내 현황 확진자 증가 추이 꺾은선 그래프')
    plt.figure(figsize=(6, 15))
    plt.show()
    plt.savefig('sample.png')