import COVID19Py as covi
import json
import sqlite3 as sl
from variable import *
from hotKeyword import *

# query create table as QCT
#print(json.dumps(post,indent = '\t', ensure_ascii=False))
sampleReque = {'bot': {'id': '5fa4d2bf6d34f06b2b08ad93', 'name': 'corona_chatbot'},
'intent': {'id': '5fb0e639d9431d64aa840e50',
'name': '전세계 현황', 'extra': {'reason': {'code': 1, 'message': 'OK'}}},
'action': {'id': '5fb8dd0e06b0fa6d6630322a', 'name': 'globalData',
'params': {'sys_nation': '미국', 'situation': 'situation'},
'detailParams': {'sys_nation': {'groupName': '', 'origin': '미국', 'value': '미국'},
'situation': {'groupName': '', 'origin': '데이터', 'value': 'situation'}},
'clientExtra': {}}, 'userRequest': {'block': {'id': '5fb0e639d9431d64aa840e50', 'name': '전세계 현황'},
'user': {'id': '28761f0d6fec519d333afb202d85dca7842acb03053fbc6e77f757a681a0732475',
'type': 'botUserKey', 'properties':
{'botUserKey': '28761f0d6fec519d333afb202d85dca7842acb03053fbc6e77f757a681a0732475',
'isFriend': True, 'plusfriendUserKey': 'IWOvhONHTgXo',
'bot_user_key': '28761f0d6fec519d333afb202d85dca7842acb03053fbc6e77f757a681a0732475',
'plusfriend_user_key': 'IWOvhONHTgXo'}}, 'utterance': '미국 데이터',
'params': {'surface': 'Kakaotalk.plusfriend'}, 'lang': 'ko', 'timezone': 'Asia/Seoul'},
'contexts': []}

def globalData(data):
    message = "None"
    try:
        #action when data['userRequest']['block']['name'] =='전세계 현황'
        #print(json.dumps(post,indent = '\t',ensure_ascii=False))
        conn=sl.connect(DB_PATH+'/corona.db')
        print(data)
        # required entity
        ntt = ['situation','sys_nation','sys_date']
        situation = ['confirmed','deaths','recovered']

        res = {'confirmed':0,'deaths':0,'recovered':0}

        data = data['action']['detailParams']
        inputNation= data['sys_nation']['value']

        if inputNation == "글로벌" or inputNation == '외국':
            inputNation = "전세계"

        originTT = '현황'

        if data['situation']['value'] == 'situation':
            # If add deaths confirmed situation
            pass

        # keyword counting for hotKeyword
        hotKeyword(inputNation + originTT)

        if inputNation in nations:
            if data['situation']['value'] == 'situation':
                    res = conn.cursor().execute("""SELECT data from GLOBAL WHERE country_code='%s' """ %(nations[input])).fetchone()
                    res = eval(res[0])

        elif data['sys_nation']['value'] == '미국':
            if data['situation']['value'] == 'situation':
                res = covi.COVID19(data_source="csbs").getLatest()
        else :
            res = '지원하지 않는 국가입니다.'
            conn.close()
            return dataSend(res)

        print(res['confirmed'])
        message = """코로나 {} 현황입니다.
확진자 {:,} 명
사망자 {:,} 명
격리해제 {:,} 명
치명률 {:.2f}%""".format(input,res['confirmed'],res['deaths'],res['recovered'],(res["deaths"]/res["confirmed"]*100))


        conn.close()
    except KeyError as e:
        print(e)
        pass
    except Exception as e:
        print(e)
        pass
    finally:
        return dataSendSimple(message)

print(globalData(sampleReque))

""" # print(dir(covi.COVID19()))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__', '_getSources', '_request',
'_update', '_valid_data_sources', 'data_source', 'getAll', 'getLatest', 'getLatestChanges',
'getLocationByCountryCode', 'getLocationById', 'getLocations', 'latestData', 'previousData', 'url']
"""
