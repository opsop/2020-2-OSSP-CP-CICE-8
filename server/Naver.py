import sqlite3
import os

item_list = []

DB_PATH = os.path.dirname(__file__) + '/CoronaBotDB'

def naver_get(param = '코로나 확진자'):
    con = sqlite3.connect(DB_PATH+"/naver.db")
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
                    }],
                    "buttons": [
                        {
                            "label": "구경가기",
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

print(naver_get())