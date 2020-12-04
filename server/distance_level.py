from hotKeyword import *

def distance_level(content):
    hotKeyword("사회적 거리두기")
    content = content['userRequest']['utterance']
    #print(content)
    dataSend = {
      "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type" : "basicCard",
                        "items": [
                            {
                                "title" : "사회적 거리두기",
                                "description" : "현재 사회적 거리두기 2단계입니다.",
                                "thumbnail": {
                                    "imageUrl": "https://user-images.githubusercontent.com/71917474/101108676-6960d200-3618-11eb-80d6-83a9a68069c5.jpg"},
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "관련 포스트 보기",
                                        "webLinkUrl": "https://m.post.naver.com/viewer/postView.nhn?volumeNo=30045858&memberNo=31572221"},
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