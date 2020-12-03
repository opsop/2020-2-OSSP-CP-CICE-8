import requests
from opengraph_py3 import OpenGraph
from bs4 import BeautifulSoup
import re
import html
import json
import pymysql

youtube_key='AIzaSyB8ZFMX5E553Q1a6z5Zrtw8Vam1GOHiY-Q'


#유튜브 뉴스
def youtubeNews():
    r = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&key={youtube_key}&q=코로나19&maxResults=5")
    j = r.json()
    youtube = []
    if list(j.keys())[0] != "error":
        for i in j['items']:
            youtube.append({
                    "title" : html.unescape(i['snippet']['title']),
                    "description" : html.unescape(i['snippet']['description']),
                    "thumbnail" : i['snippet']['thumbnails']['high']['url'],
                    "channelTitle" : i['snippet']['channelTitle'],
                    "link" : f"https://www.youtube.com/watch?v={i['id']['videoId']}"
                })
    #cursor.execute("UPDATE `data` SET `youtube`=%s", json.dumps(youtube))
    return youtube