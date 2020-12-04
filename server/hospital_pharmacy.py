from flask import Flask, request
import json
from hotKeyword import *

imageUrl = "https://user-images.githubusercontent.com/71917474/100836760-37822b00-34b3-11eb-8808-680db10567ce.jpg"


def hospital_info(content):
    # content = request.get_json()
    #content = json.loads(request.data)
    # print(content)
    hotKeyword("근처 병원 및 약국 안내")
    content = content['userRequest']['utterance']
    # print(content)

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": "병원 안내",
                                "description": "주변 병원 위치 안내",
                                "thumbnail": {
                                    "imageUrl": imageUrl},
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "카카오맵 바로가기",
                                        "webLinkUrl": "https://map.kakao.com/link/search/병원"},
                                    {
                                        "action": "share",
                                        "label": "공유하기"}
                                ]
                            },
                            {
                                "title": "약국 안내",
                                "description": "주변 약국 위치 안내",
                                "thumbnail": {
                                    "imageUrl": imageUrl},
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "카카오맵 바로가기",
                                        "webLinkUrl": "https://map.kakao.com/link/search/약국"},
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