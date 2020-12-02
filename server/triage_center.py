from flask import Flask, request
import json

imageUrl = "https://user-images.githubusercontent.com/71917474/100836760-37822b00-34b3-11eb-8808-680db10567ce.jpg"


def triage(content):
    # content = request.get_json()
    #content = json.loads(request.data)
    # print(content)
    content = content['userRequest']
    content = content['utterance']
    print(content)

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": "선별진료소 안내",
                                "description": "주변 선별진료소 위치 안내",
                                "thumbnail": {
                                    "imageUrl": imageUrl},
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "카카오맵 바로가기",
                                        "webLinkUrl": "https://map.kakao.com/link/search/선별진료소"},
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