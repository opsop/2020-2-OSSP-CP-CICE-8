from hotKeyword import *

def self_diagnosis(content):
    hotKeyword("자가진단")
    content = content['userRequest']['utterance']
    #print(content)
    dataSend = { "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type" : "basicCard",
                        "items": [
                            {
                                "title" : "코로나 자가진단 테스트",
                                "description" : "총 8문항의 질문으로 코로나 자가진단 테스트를 실시합니다.",
                                "thumbnail": {
                                    "imageUrl": "https://user-images.githubusercontent.com/71917474/100963699-4d065c00-356a-11eb-9c7f-b94780fd48aa.png"},
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자가진단 하러가기",
                                        "webLinkUrl": "http://aiselftest.com/covid/"},
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