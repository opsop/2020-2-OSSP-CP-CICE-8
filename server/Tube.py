import sqlite3
import os

item_list = []

DB_PATH = os.path.dirname(__file__) + '/CoronaBotDB'

def tube_get(param = '코로나 확진자'):
    con = sqlite3.connect(DB_PATH+"/tube.db")
    res = con.cursor().execute("""SELECT * from NEWS WHERE CATEGORY='%s' """ % (param)).fetchall()

    card = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "listCard": {
                    "header": {
                        "title": "유튜브 뉴스"
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
                            "label": "관련 뉴스 더 보기",
                            "action": "webLink",
                            "webLinkUrl": f"https://www.youtube.com/results?search_query={param.replace(' ','+')+'+뉴스'}"
                        }
                    ]
                }

            }
        ]
    }
}

    return card

print(tube_get())