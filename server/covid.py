import COVID19Py as covi
import json
##covid19 = covi.COVID19()
#data = covid19.getAll()
#print(json.dumps(data,indent = '\t'))
""" # print(dir(covi.COVID19()))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__', '_getSources', '_request',
'_update', '_valid_data_sources', 'data_source', 'getAll', 'getLatest', 'getLatestChanges',
'getLocationByCountryCode', 'getLocationById', 'getLocations', 'latestData', 'previousData', 'url']
"""
post = {'bot': {'id': '5fa4d2bf6d34f06b2b08ad93!', 'name': 'corona_chatbot'},
'intent': {'id': '5fb0e639d9431d64aa840e50', 'name': '전세계 현황', 'extra': {'reason': {'code': 1, 'message': 'OK'}}}, 'action': {'id': '5fb0d8e5e0729d24a9b0b1af', 'name': 'server_test', 'params': {'situation1': 'situation', 'sys_date': '{"date": "2020-11-21", "dateTag": "today", "dateHeadword": null, "year": null, "month": null, "day": null}', 'situation': '현황', 'sys_nation': '미국'}, 'detailParams': {'situation1': {'groupName': '', 'origin': '현황', 'value': 'situation'}, 'sys_date': {'groupName': '', 'origin': '오늘', 'value': '{"date": "2020-11-21", "dateTag": "today", "dateHeadword": null, "year": null, "month": null, "day": null}'}, 'situation': {'groupName': '', 'origin': '현황', 'value': 'situation'}, 'sys_nation': {'groupName': '', 'origin': '미국', 'value': '전세계'}}, 'clientExtra': {}}, 'userRequest': {'block': {'id': '5fb0e639d9431d64aa840e50', 'name': '전세계 현황'}, 'user': {'id': '28467d86be10408615c5ca4d2800eb01ca2acb03053fbc6e77f757a681a0732475', 'type': 'botUserKey', 'properties': {'botUserKey': '28467d86be10408615c5ca4d2800eb01ca2acb03053fbc6e77f757a681a0732475', 'bot_user_key': '28467d86be10408615c5ca4d2800eb01ca2acb03053fbc6e77f757a681a0732475'}}, 'utterance': '오늘 미국 코로나 현황 알려줘\n', 'params': {'surface': 'BuilderBotTest', 'ignoreMe': 'true'}, 'lang': 'kr', 'timezone': 'Asia/Seoul'}, 'contexts': []}
#print(json.dumps(post,indent = '\t', ensure_ascii=False))


def globalData(data):
    #action when data['userRequest']['block']['name'] =='전세계 현황'
    #print(json.dumps(post,indent = '\t',ensure_ascii=False))

    # required entity
    entity = ['situation','sys_nation','sys_date']
    situation = ['confirmed','deaths','recovered']

    data = data['action']['detailParams']
    res = 'None'

    if data['sys_nation']['value'] == '전세계':
        if data['situation']['value'] == 'situation':
            res = covi.COVID19().getLatest()

    elif data['sys_nation']['value'] == '미국':
        if data['situation']['value'] == 'situation':
            res = covi.COVID19(data_source="csbs").getLatest()

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText":{
                        "text" : str(json.dumps(res,indent='\t'))
                    }
                }
            ]
        }
    }

    return dataSend
#globalData(post)
