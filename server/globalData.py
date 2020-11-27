import COVID19Py as covi
import json
import sqlite3 as sl
from variable import *
# query create table as QCT
#print(json.dumps(post,indent = '\t', ensure_ascii=False))


def globalData(data):
    #action when data['userRequest']['block']['name'] =='전세계 현황'
    #print(json.dumps(post,indent = '\t',ensure_ascii=False))
    conn=sl.connect(DB_PATH+'/corona.db')
    print(data)
    # required entity
    entity = ['situation','sys_nation','sys_date']
    situation = ['confirmed','deaths','recovered']

    res = {'confirmed':0,'deaths':0,'recovered':0}

    data = data['action']['detailParams']
    input= data['sys_nation']['value']

    if input in nations:
        if data['situation']['value'] == 'situation':
                res = conn.cursor().execute("""SELECT data from GLOBAL WHERE country_code='%s' """ %(nations[input])).fetchone()
                print(res)
                res = eval(res[0])
                print(type(res))

    elif data['sys_nation']['value'] == '미국':
        if data['situation']['value'] == 'situation':
            res = covi.COVID19(data_source="csbs").getLatest()
    else :
        res = '지원하지 않는 국가입니다.'
        conn.close()
        return dataSend(res)

    print(res['confirmed'])
    message = """%s 현황입니다.
    확진자 %d 명
    사망자 %d 명
    격리해제 %d 명입니다.
    """ %(input,res['confirmed'],res['deaths'],res['recovered'])


    conn.close()
    return dataSend(message)


def dataSend(message):

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText":{
                        "text" : message
                    }
                }
            ]
        }
    }

    return dataSend

""" # print(dir(covi.COVID19()))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__', '_getSources', '_request',
'_update', '_valid_data_sources', 'data_source', 'getAll', 'getLatest', 'getLatestChanges',
'getLocationByCountryCode', 'getLocationById', 'getLocations', 'latestData', 'previousData', 'url']
"""
