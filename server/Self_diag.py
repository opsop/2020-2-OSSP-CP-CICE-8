from hotKeyword import *

'''
코로나 자가진단, 코로나 블루 자가진단 테스트와 연결해주고,
링크를 다른 카톡 사용자들과 공유할 수 있음
'''

def self_diagnosis(content):
    hotKeyword("자가진단")
    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": "코로나 자가진단",
                                "description": "총 8개의 문항으로 하는 코로나 감염증 사전참고 테스트 입니다. 감염 의심시 콜센터('1339' 또는 '지역번호+120')로 연락하신 후 자가격리 하시면 됩니다.",
                                "thumbnail": {
                                    "imageUrl": "https://user-images.githubusercontent.com/48379869/101219822-eeef8b00-36c7-11eb-801b-950fc81992c5.png"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자가진단 하러가기",
                                        "webLinkUrl": "http://aiselftest.com/covid/"},
                                    {
                                        "action": "share",
                                        "label": "공유하기"}
                                ]
                            },
                            {
                                "title": "코로나 블루 자가진단",
                                "description": "몸보다 마음이 더 힘들어요... 나도 혹시 코로나 블루?",
                                "thumbnail": {
                                    "imageUrl": "https://user-images.githubusercontent.com/48379869/101220311-d0d65a80-36c8-11eb-9048-65719ec7e408.png"},
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자가진단 하러가기",
                                        "webLinkUrl": "https://trost.co.kr/promotion/channel/covid-19-with-depressive/"},
                                    {
                                        "action": "share",
                                        "label": "공유하기"}
                                ]
                            }
                        ]
                    }
                }
            ]
        }
    }

    return dataSend