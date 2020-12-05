from django.shortcuts import render
from django.http import HttpResponse
# from django.core import serializers
from django.contrib import messages
from . import keyword 
from .models import StatisticValues
from datetime import datetime
import json


# Create your views here.
def index(request):
    #============================================ Start of 'contents-home.html' ====================================================
    #통계 받아오는 API로 가져옴
    result = keyword.keywordFindAPI()
    #print(result)
    #context는 html에 data로 넘겨주는 parameter들을 담는것. 각각의 값을 전달한다
    #예를 들어 context에 result, result2, result3 이렇게 넣어서 전달하면
    #index.html에서 result, result2, result3 변수를 html 태그나 javascript코드 등에서 사용 가능하다.
    
    '''
    statisticDB = StatisticValues.objects.all() # 테이블 데이타를 전부 가져오기 위한 메소드
    statisticDBValues = list(StatisticValues.objects.all().values())
    context ={
        'result' : result,
        'statisticDBValues' : statisticDBValues,
    }
    print(statisticDBValues)
    '''
    # API 데이터를 DB 테이블 StatisticValues에 저장.
    try :
        
        YEAR= datetime.today().year        # 현재 연도 가져오기
        #TodayDate=str(YEAR)+"."+str(MONTH)+"."+str(DAY)
        #print(TodayDate)
        # if statisticDB.objects.get(updateTime=TodayDate).updateTime != TodayDate:
        #if not statisticDB.objects.filter(updateTime=TodayDate).exists(): 
        statisticValue = StatisticValues(updateTime = str(YEAR)+"."+result['updateTime'][23:28], 
                             TotalCase = result['TotalCase'], 
                             TotalDeath = result['TotalDeath'], TotalRecovered = result['TotalRecovered'],
                             NowCase = result['NowCase'], TotalChecking = result['TotalChecking'],
                             TodayCase = result['data0_1'], TodayRecovered =result['TodayRecovered'])
        statisticValue.save()
        
    except Exception as e:
        print(e)
        statisticValue  = None
    # updateTime # 정보 업데이트 시간 data['updateTime'][23:28] -> 월.일(00.00 구조)

    statisticDB = StatisticValues.objects.all() # 테이블 데이타를 전부 가져오기 위한 메소드
    statisticDBValues = list(StatisticValues.objects.all().values())
    
    #print(statisticDBValues)
    #print(statisticValue)
    #=============================================== End of 'contents-home.html' ========================================================
    context = {
        # contents-home
        'result' : result,
        'statisticDBValues': statisticDBValues,
    }
    return render(request, 'statistic.html', context)
    #return render(request, 'index.html', context)