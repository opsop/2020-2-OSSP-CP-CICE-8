import sqlite3
import os
DB_PATH = os.path.dirname(__file__) + '/CoronaBotDB'

def KoreaCorona(param):
    con = sqlite3.connect(DB_PATH + '/newkorea.db')
    cur = con.cursor()
    cur.execute("select * from korea where rowid = 7")
    # 데이터 Fetch
    rows = cur.fetchall()
    row = rows[0]
    messages = """(%s 00시 기준)
확진자 %s(+%s)명
완치자 %s(+%s)명
사망자 %s명
격리자 %s명
치명률 %.2f%%""" % (row[0],
                 row[1], row[5],
                 row[2], row[7],
                 row[4],
                 row[3],
                 int(row[4]) / int(row[1]) * 100)  # 치명률: (사망자/ 확진자)*100

    if param == "현황 보기":
        return KoreadataSendCard(messages,
                                 imageUrl="https://user-images.githubusercontent.com/71917474/101284898-d39a9200-3825-11eb-9474-44084a8631de.jpg")
    elif param == "추이 그래프":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            "imageUrl": "https://github.com/CSID-DGU/2020-2-OSSP-CP-CICE-8/blob/main/server/korea_graph.png?raw=true",
                            # 직접 만든 시각화 이미지의 URL
                            "altText": "국내 코로나 확진자 추이입니다."
                        }
                    }
                ]
            }
        }
    else:  # 현황보기/ 추이 그래프가 입력되지 않은 경우.
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "다시 입력해주세요."
                        }
                    }
                ]
            }
        }

    return dataSend


def KoreadataSendCard(message, imageUrl):
    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": "국내 코로나 현황",
                                "description": message,
                                "thumbnail": {
                                    "imageUrl": imageUrl},
                                "buttons": [
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