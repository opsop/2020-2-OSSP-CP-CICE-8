import COVID19Py as covi
import json
import sqlite3 as sl
from ConstVar import *
from hotKeyword import *
from copy import deepcopy
from ConstVar import imageUrl
# query create table as QCT
#print(json.dumps(post,indent = '\t', ensure_ascii=False))


def globalData(data):
    message = "None"
    try:
        #action when data['userRequest']['block']['name'] =='전세계 현황'
        #print(json.dumps(post,indent = '\t',ensure_ascii=False))
        conn=sl.connect(DB_PATH+'/corona.db')
        #print(data)
        # required entity
        ntt = ['situation','sys_nation','sys_date']
        situation = ['confirmed','deaths','recovered']

        res = {'confirmed':0,'deaths':0,'recovered':0}

        data = data['action']['detailParams']
        inputNation= deepcopy(data['sys_nation']['value'])

        if inputNation == "글로벌" or inputNation == '외국':
            inputNation = "전세계"

        originTT = '현황'

        if data['situation']['value'] == 'situation':
            # If add deaths confirmed situation
            pass

        # keyword counting for hotKeyword
        hotKeyword(inputNation +" "+ originTT)

        if inputNation in nations:
            if data['situation']['value'] == 'situation':
                res = conn.cursor().execute("""SELECT data from GLOBAL WHERE country_code='%s' """ %(nations[inputNation])).fetchone()
                res = eval(res[0])

        elif data['sys_nation']['value'] == '미국':
            if data['situation']['value'] == 'situation':
                res = covi.COVID19(data_source="csbs").getLatest()
        else :
            res = '지원하지 않는 국가입니다.'
            conn.close()
            return dataSend(res)
        update = conn.cursor().execute("select LASTUPDATE from global").fetchone()[0].split("T")[0].replace("-",".")
        #print(res['confirmed'])
        message = """({} 기준)
확진자 {:,}명
사망자 {:,}명
격리해제 {:,}명
치명률 {:.2f}%""".format(update,res['confirmed'],res['deaths'],res['recovered'],(res["deaths"]/res["confirmed"]*100))


        conn.close()
    except KeyError as e:
        print("KeyError" ,e)
        print(traceback.format_exc())
    except Exception as e:
        print("Exception",e)
        print(traceback.format_exc())
    finally:
        return GlobaldataSendCard(data['sys_nation']['value'],message,imageUrl = imageUrl )

#print(globalData(sampleReque))

""" # print(dir(covi.COVID19()))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__', '_getSources', '_request',
'_update', '_valid_data_sources', 'data_source', 'getAll', 'getLatest', 'getLatestChanges',
'getLocationByCountryCode', 'getLocationById', 'getLocations', 'latestData', 'previousData', 'url']
"""
