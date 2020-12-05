import sqlite3
import os
from hotKeyword import *

item_list = []

DB_PATH = os.path.dirname(__file__) + '/CoronaBotDB'

def naver_get(param = '코로나 확진자'):
    hotKeyword("네이버 뉴스")

    '''
        기타 검색일 때, '코로나' 검색어로
        네이버 뉴스에 검색한 링크 반환
        (simpleText형태)
    '''

    '''
    주어진 엔티티 (corona_topic)
    : 코로나 확진자, 코로나 백신, 코로나 후유증
    '''

    '''
        주어진 엔티티일 때, 해당 검색어로
        db로 저장된 제목, 발행일자, 사진, 링크를 꺼내서
        5개까지 보여주고,
        해당 검색어로 네이버 뉴스 검색 링크와 연결하는 버튼도 보여줌
        (List Card 형태)
    '''

    if param == "기타 검색":
        output = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={'코로나'}"
                    }
                }
            ]
        }
        }
        return output

    else:
        con = sqlite3.connect(DB_PATH + "/naver.db")
        res = con.cursor().execute("""SELECT * from NEWS WHERE ENTITY='%s' """ % (param)).fetchall()

        card = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "네이버 뉴스"
                        },
                        "items": [

                            {
                                "title": res[0][1],
                                "description": res[0][2],
                                "imageUrl": res[0][3],
                                "link": {
                                    "web": res[0][4]
                                }
                            },
                            {
                                "title": res[1][1],
                                "description": res[1][2],
                                "imageUrl": res[1][3],
                                "link": {
                                    "web": res[1][4]
                                }
                            }
                        ,

                        {
                            "title": res[2][1],
                            "description": res[2][2],
                            "imageUrl": res[2][3],
                            "link": {
                                "web": res[2][4]
                            }
                        },

                        {
                            "title": res[3][1],
                            "description": res[3][2],
                            "imageUrl": res[3][3],
                            "link": {
                                "web": res[3][4]
                            }
                        },

                    {
                        "title": res[4][1],
                        "description": res[4][2],
                        "imageUrl": res[4][3],
                        "link": {
                            "web": res[4][4]
                        }
                    }],

                        "buttons": [
                            {
                                "label": param+" 기사 더보기",
                                "action": "webLink",
                                "webLinkUrl": f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={param.replace(' ','+')}"
                            }
                        ]
                    }

                }
            ]
        }
        }

        return card

# 파라미터 자체는 띄어쓰기로 들어왔어도, 검색창 링크는 띄어쓰기를 +로 바꿔줘야함
print(naver_get('코로나 백신'))