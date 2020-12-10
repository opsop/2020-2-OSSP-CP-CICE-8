from flask import Flask, request
import json
from hotKeyword import *

imageUrl = "https://user-images.githubusercontent.com/71917474/100836760-37822b00-34b3-11eb-8808-680db10567ce.jpg"


def mask_info(content):
    hotKeyword("마스크")
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
                            },
                            {
                                "title": "편의점 안내",
                                "description": "주변 편의점 위치 안내",
                                "thumbnail": {
                                    "imageUrl": imageUrl},
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "카카오맵 바로가기",
                                        "webLinkUrl": "https://map.kakao.com/link/search/편의점"},
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